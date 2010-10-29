from django.conf.urls.defaults import *

urlpatterns = patterns('pages.views',
    url(r'^$', 'page_index', name = 'page_index'),
    url(r'(?P<page_id>\d+)/$', 'page_show', name = 'page_show'),
)
