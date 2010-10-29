from django.conf.urls.defaults import *

urlpatterns = patterns('recipes.views',
    url(r'^$', 'recipe_index', name = 'recipe_index'),
    url(r'(?P<recipe_id>\d+)/$', 'recipe_show', name = 'recipe_show'),
)
