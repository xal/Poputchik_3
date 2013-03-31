from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings

class DelAdminFileWidget(AdminFileWidget):
    '''
    A AdminFileWidget that shows a delete checkbox
    '''
    input_type = 'file'

    def render(self, name, value, attrs=None):
        input = super(forms.widgets.FileInput, self).render(name, value, attrs)
        if value:
            output = []
            output.append('%s %s' % (_('Currently:'), '<a target="_blank" href="%s%s">%s</a>' % (settings.MEDIA_URL, value, value)))
            output.append('%s %s' % (_('Change:'), input))
            output.append('%s %s' % (_('Delete') + ':', '<input type="checkbox" name="%s_delete"/>' % name))
            return mark_safe(u'<div style="float: left;">' + u'<br/>'.join(output) + u'</div>')
        else:
            return mark_safe(input)

    def value_from_datadict(self, data, files, name):
        if not data.get('%s_delete' % name):
            return super(DelAdminFileWidget, self).value_from_datadict(data, files, name)
        else:
            return '__deleted__'

