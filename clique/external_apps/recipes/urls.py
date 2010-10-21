from django.conf.urls.defaults import *

urlpatterns = patterns('recipes.views',
    (r'^/$', 'recipe_index', name = 'recipe_index'),
    (r'^(?<recipe_id>)/$', 'recipe_show', name = 'recipe_show'),
)