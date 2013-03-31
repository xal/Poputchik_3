import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404
from models import Page, Slider, Testimonial
from forms import *
import contact as contact_module


def simple(template):
    def d1(func):
        def d2(request, *args, **kwargs):
            r = func(request, *args, **kwargs)
            if isinstance(r, HttpResponse):
                return r
            else:
                return render_to_response(template, r, context_instance=RequestContext(request))
        return d2
    return d1

def make_rows(lst, per_row=6):
    for i in xrange((len(lst) + per_row - 1) // per_row):
        yield lst[i * per_row: i * per_row + per_row]

def pick_one(q):
    for i in q:
        return i
    return None

@simple('index.html')
def index(request):
    page = None
    slides = None
    testimonials = None
    try:
        page = pick_one(Page.objects.filter(slug='index'))
        a = 1
        b = 2
        c = a + b
    except:
        pass
    return {
        'page': page,
        'a': datetime.datetime.utcnow() ,
    }

@simple('page.html')
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return {
        'page': page,
    }

@simple('contact.html')
def contact(request):
    page = pick_one(Page.objects.filter(slug='contact-us'))
    form, success = contact_module.handle_form('contact-us', request, ContactForm)
    if success:
        return HttpResponseRedirect('/thank-you')
    return {
        'page': page,
        'form': form,
    }

@simple('thank_you.html')
def thank_you(request):
    page = pick_one(Page.objects.filter(slug='thank-you'))
    return {
        'page': page,
        }
