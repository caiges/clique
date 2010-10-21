from django.conf.urls.defaults import *

urlpatterns = patterns('recipes.views',
    (r'^/$', 'category_index', name = 'category_index'),
    (r'^(?<category_id>)/$', 'category_show', name = 'category_show'),
)