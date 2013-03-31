from django import forms
from django.contrib import admin
from models import Form, Recipient, History, BlacklistItem

# Form

class RecipientAdmin(admin.TabularInline):
    model = Recipient
    extra = 1

class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_subject')
    inlines = (RecipientAdmin,)

    template_help_text = '''<p>
    <b>{{ data }}</b> - placeholder for whole received data<br>
    <b>{{ ip }}</b> - placeholder for IP address of a site visitor<br>
    <b>{{ created }}</b> - placeholder for a date and time message is received<br>
    <b>{{ created|date }}</b> - placeholder for a date<br>
    <b>{{ created|time }}</b> - placeholder for a time of day<br>
    <b>{{ host }}</b> - placeholder for a hame of site
    </p>'''

    def formfield_for_dbfield(self, db_field, **kwargs):
        x = super(FormAdmin, self).formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == 'name':
            x.help_text = 'Internal identifier. Do not change it!'
        elif db_field.name == 'sender':
            x.help_text = 'Default sender.'
        elif db_field.name == 'sender_field':
            x.help_text = 'Use visitor\'s e-mail as sender. Usually this field is called "email".'
        elif db_field.name == 'email_subject':
            x.help_text = self.template_help_text
        elif db_field.name == 'email_text':
            x.widget.attrs.update({
                'style': 'width:700px; height:300px;'
            })
            x.help_text = self.template_help_text
        return x

    class Media:
        js = ['js/jquery.js', 'js/jquery.tinymce.js', 'js/admin_tinymce.js']

admin.site.register(Form, FormAdmin)

# History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip', 'form')
    list_filter = ('form',)
    date_hierarchy = 'created'
admin.site.register(History, HistoryAdmin)

# BlacklistItem

class BlacklistItemForm(forms.ModelForm):
    class Meta:
        model = BlacklistItem

    def clean_ip(self):
        ip = self.cleaned_data['ip']
        l = ip.split('.')
        if len(l) != 4:
            raise forms.ValidationError('IP address has an invalid format.')
        ip = []
        for n in l:
            n = int(n)
            if n < 0 or n > 255:
                raise forms.ValidationError('IP address has an invalid format.')
            ip.append(str(n))
        return '.'.join(ip)

class BlacklistItemAdmin(admin.ModelAdmin):
    form = BlacklistItemForm
    list_display = ('ip', 'comment')

admin.site.register(BlacklistItem, BlacklistItemAdmin)

