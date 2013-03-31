from annoying.templatetags import smart_if
import django
from django import template


register = template.Library()


try:
    if int(django.get_version()[-5:]) < 11806:
        register.tag('if', smart_if)
except ValueError:
    pass
