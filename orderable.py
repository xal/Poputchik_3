import re
import urllib
from django.db import models
from django.shortcuts import redirect
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

class OrderField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['null'] = True
        kwargs['blank'] = True
        kwargs['editable'] = True
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if not getattr(model_instance, self.attname):
            m = model_instance.__class__.objects.aggregate(o=models.Max(self.attname))['o'] or 0
            setattr(model_instance, self.attname, m + 1)
        return super(OrderField, self).pre_save(model_instance, add)

url = (r'^reorder/', 'orderable.reorder')


class OrderableAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        self.list_display += ('reorder', )
        super(OrderableAdmin, self).__init__(*args, **kwargs)

    def reorder(self, obj):
        if hasattr(self, 'ordering_extra_filter'):
            extra_filter = self.ordering_extra_filter(obj)
        else:
            extra_filter = {}
        q = urllib.urlencode(extra_filter)
        i = (obj._meta.app_label, obj._meta.module_name, obj.id, q)
        u = '/reorder/%s/%s/%d/move-up/?%s' % i
        d = '/reorder/%s/%s/%d/move-down/?%s' % i
        return '<a href="%s">Move&nbsp;Up</a>&nbsp;|&nbsp;<a href="%s">Move&nbsp;Down</a>' % (u, d)
    reorder.short_description = 'Order'
    reorder.allow_tags = True


def _find_order_field_name(obj):
    for field_name in obj._meta.get_all_field_names():
        try:
            field = obj._meta.get_field(field_name)
            if isinstance(field, OrderField):
                return field_name
        except:
            pass
    return None

def find_prev(obj, field_name=None, extra_filter={}):
    field_name = field_name or _find_order_field_name(obj)
    f = {field_name + '__lt': getattr(obj, field_name)}
    if extra_filter:
        f.update(extra_filter)
    for o in obj.__class__.objects.filter(**f).order_by('-' + field_name)[:1][:1]:
        return o
    return None

def find_next(obj, field_name=None, extra_filter={}):
    field_name = field_name or _find_order_field_name(obj)
    f = {field_name + '__gt': getattr(obj, field_name)}
    if extra_filter:
        f.update(extra_filter)
    for o in obj.__class__.objects.filter(**f).order_by(field_name)[:1]:
        return o
    return None

def swap(obj1, obj2, field_name=None):
    field_name = field_name or _find_order_field_name(obj1)
    o1 = getattr(obj1, field_name)
    o2 = getattr(obj2, field_name)
    setattr(obj1, field_name, o2)
    setattr(obj2, field_name, o1)
    obj1.save()
    obj2.save()

def reorder(request):
    m = re.search(r'^/reorder/(.*?)/(.*?)/(.*?)/move-(up|down)/$', request.path)
    if m:
        user_type = ContentType.objects.get(app_label=m.group(1), model=m.group(2))
        obj = user_type.get_object_for_this_type(id=m.group(3))
        field_name = _find_order_field_name(obj)

        extra_filter = {}
        for k, v in request.GET.iteritems():
            extra_filter[str(k)] = v

        if m.group(4) == 'up':
            other = find_prev(obj, field_name, extra_filter)
        else:
            other = find_next(obj, field_name, extra_filter)
        if other:
            swap(obj, other, field_name)

    r = request.REQUEST.get('redirect') or request.META.get('HTTP_REFERER') or '/'
    return redirect(r)

