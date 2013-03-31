import json
from django.db import models
from django.template.loader import get_template_from_string
from django.conf import settings
from django.template import Context
from django.template.loader import get_template_from_string
from django.core.validators import validate_email
from django.core.mail import EmailMessage, mail_admins
import settings as settings
import os

def create_form_table(form):
    s = '<table style="border-collapse: collapse;">'
    for field in form:
        s += '<tr><th style="border:1px solid #ccc; text-align: left; padding: 0.6em;">%s</th><td style="border:1px solid #ccc; text-align: left; padding: 0.6em;">%s</td></tr>' % (field.label, form.cleaned_data.get(field.name, ''))
    s += '</table>'
    return s

DEFAULT_EMAIL_SUBJECT = 'New Web Submission'

DEFAULT_EMAIL_TEXT = '''
<p>Hello <strong>{{ user }}</strong>,</p>
<p>Someone has submitted the contact form at <strong>{{ host }}</strong>:<br />
The request was submitted on <strong>{{ created|date }}</strong> at <strong>{{ created|time }}</strong> from the IP address of <strong>{{ ip }}</strong>.</p>
<p>Request details:</p>
<p>{{ data }}</p>
<p>Truly yours,<br />
Mailer daemon @ <strong>{{ host }}</strong></p>'''

class Form(models.Model):
    name = models.CharField(max_length=255, unique=True)

    sender = models.EmailField(max_length=255, null=True, blank=True)
    sender_field = models.CharField(max_length=128, null=True, blank=True)

    email_subject = models.CharField(max_length=255, default=DEFAULT_EMAIL_SUBJECT)
    email_text = models.TextField(default=DEFAULT_EMAIL_TEXT)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.name

    def get_sender(self, form):
        if self.sender_field.strip():
            try:
                result = form.cleaned_data.get(self.sender_field.strip(), '')
                validate_email(result)
                return result
            except:
                pass
        if self.sender:
            return self.sender
        return 'contact@liftboss.icmconsulting.com'

    def handle_uploaded_file(self, f):
        dirname = 'tmp'
        dest_dir = os.path.join(settings.MEDIA_ROOT, dirname)
        filename = os.path.join(dest_dir, f.name)
        fi = open(filename, 'wb+')
        for chunk in f.chunks():
            fi.write(chunk)
        return filename

    def handle_form(self, request, form_class, file=None):
        if request.method == 'POST':
            f = form_class(request.POST)
            if f.is_valid():
                history = History()
                history.form = self
                history.ip = request.META.get("REMOTE_ADDR", u"127.0.0.1")
                history.data = json.dumps([(field.label, f.cleaned_data.get(k, '')) for k, field in f.fields.iteritems()])
                history.save()

                table = create_form_table(f)
                ctx = Context({
                    'data': table,
                    'ip': history.ip,
                    'created': history.created,
                    'host': request.META.get('HTTP_HOST', 'your website'),
                })
                try:
                    if file:
                        filename = self.handle_uploaded_file(request.FILES['file'])
                        history.file = os.path.join('tmp', request.FILES['file'].name)
                        history.save()
                    sender = self.get_sender(f)
                    for r in self.recipients.filter(active=True):
                        ctx['user'] = r.name or 'Admin'
                        subject = get_template_from_string(u'{%% autoescape off %%}%s{%% endautoescape %%}' % self.email_subject).render(ctx)
                        message = get_template_from_string(u'{%% autoescape off %%}%s{%% endautoescape %%}' % self.email_text).render(ctx)
                        msg = EmailMessage(subject, message, sender, [r.email])
                        if file:
                            msg.attach_file(filename)
                        msg.content_subtype = "html"
                        msg.send()
                except Exception, e:
                    import traceback
                    host = request.META.get('HTTP_HOST', 'Unknown host')
                    message = host + '\n\n' + unicode(e) + '\n\n' + traceback.format_exc()
                    mail_admins('Sending contact email failed.', message, fail_silently=True)

                return f, True
        else:
            f = form_class()
        return f, False


class Recipient(models.Model):
    form = models.ForeignKey(Form, related_name='recipients')
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email


class History(models.Model):
    form = models.ForeignKey(Form)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=128, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='tmp', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return 'Contact %s / %s' % (self.created, self.ip)

    def get_data(self):
        return json.loads(self.data)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Contact History'
        verbose_name = 'Contact History'

class BlacklistItem(models.Model):
    ip = models.CharField(max_length=15)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name_plural = 'Blacklist'
        verbose_name = 'Blacklist item'

