from django.conf.urls import patterns, include, url
from django.contrib import admin
# from simplereg.forms import LoginForm

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sm.views.home', name='home'),
                       # url(r'^sm/', include('sm.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^polls/', include('nm.urls', namespace="nm")),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'nm.views.home', name='home'),

                       # url(r'^registration/', include('nm.urls', namespace="nm")),
                       # url(r'^login/', include('nm.urls', namespace="nm")),

                       # url(r'^registration/$', 'simplereg.views.registration', {
                       #     'template_name': 'registration.html',
                       #     'autologin': True,
                       #     'callback': None
                       # }, name='registration'),
                       # url(r'^login/$', 'django.contrib.auth.views.login', {
                       #     'template_name': 'login.html',
                       #     'authentication_form': LoginForm
                       # }, name='login'),
)