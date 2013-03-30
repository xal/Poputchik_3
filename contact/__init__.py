from models import Form, BlacklistItem

def handle_form(form_name, request, form_class, pdf=None):
    return Form.objects.get(name=form_name).handle_form(request, form_class, pdf)

def is_blocked_ip(ip):
    return not ip or BlacklistItem.objects.filter(ip=ip).count() == 0

def is_blocked(request):
    return is_blocked_ip(request.META.get('REMOTE_ADDR'))

