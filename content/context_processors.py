import re
from models import SiteElement


def site_elements(request):
    d = {}
    for s in SiteElement.objects.all():
        n = re.sub(r'\W+', '_', s.name).lower()
        d[n] = s.value
    return {
        'se': d,
    }
