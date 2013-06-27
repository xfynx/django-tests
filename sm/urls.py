from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sm.views.home', name='home'),
    # url(r'^sm/', include('sm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^poll/', include('nm.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
