import os

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.index'),
    (r'^articles/(P<url>.*)$', 'core.views.article_show'),
    (r'^content-association/content_items.json', 'core.views.content_association'),
    (r'^content-association/content_items/remove.json', 'core.views.remove_content_association'),
    (r'^association-test/', 'core.views.association_test'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^pages/', include('external_apps.pages.urls')),
    (r'^products/', include('external_apps.products.urls')),
    (r'^recipes/', include('external_apps.recipes.urls')),
    (r'^admin/contentassocation/$', include('external_apps.contentassociation.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
