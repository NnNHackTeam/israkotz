from django.conf.urls import patterns, include, url
from surlex.dj import surl
from surlex import register_macro
from piston.resource import Resource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from IsraKotzApp.handler import BudgetHandler

budgetHandler = Resource(BudgetHandler)

register_macro('t', r'.+')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'israkotz.views.home', name='home'),
    # url(r'^israkotz/', include('israkotz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'IsraKotzApp.views.home', name='home'),
    surl(r'^budget/<city:t>/$', budgetHandler),
    url(r'^autocomplete_city/$', 'IsraKotzApp.views.autocomplete_city', name='autocomplete_city'),

)
# admin.autodiscover()

