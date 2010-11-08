from django.conf.urls.defaults import *

urlpatterns = patterns('tags.views',
    url(r'^$', 'tag_index', name = 'tag_index'),
    url(r'(?P<tag_id>\d+)/$', 'tag_show', name = 'tag_show'),
)
