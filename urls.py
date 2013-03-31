from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
import orderable

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    orderable.url,
)

if settings.STATIC_SERVE_ROOT is not None:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_SERVE_ROOT, 'show_indexes': False}),
    )

urlpatterns += patterns('',
    url(r'^$', 'content.views.index'),
    url(r'^contact-us$', 'content.views.contact'),
    url(r'^thank-you$', 'content.views.thank_you'),
    url(r'^auth/', include('publicauth.urls')),
    url(r'^products/(.*)', 'product.views.product'),
    url(r'^products', 'product.views.products'),
    url(r'^portfolios', 'portfolio.views.portfolios'),
    url(r'^portfolio/(.*)', 'portfolio.views.get_portfolio'),
    url(r'^company/(.*)', 'company.views.company'),
    url(r'^companies', 'company.views.companies'),
    url(r'^(.*)$', 'content.views.page'),
)
