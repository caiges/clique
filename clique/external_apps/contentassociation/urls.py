from django.conf.urls.defaults import *

urlpatterns = patterns('contentassociation.views',
    url(r'^conflicts/', 'admin_conflicts_show', name = 'admin_conflicts_show'),
)
