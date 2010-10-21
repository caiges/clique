import os

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^/', 'core.views.index'),
    (r'^content-association/content_items.json/$', 'core.views.item_association'),
    (r'^association-test/', 'core.views.association_test'),
    (r'^products/', include('external_apps.products.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)