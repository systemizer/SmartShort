from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('smartshort.main.views',
    url(r'^extension/get/$', 'extension_get'),
    url(r'^extension/create/$', 'extension_create'),
    url(r'^get/$', 'get'),
)
