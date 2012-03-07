from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('smartshort.main.views',
    url(r'^extension/get/$', 'extension_get'),
    url(r'^extension/create/$', 'extension_create'),
    url(r'^how-it-works/', 'how_it_works'),
    url(r'^$', 'get'),

)
