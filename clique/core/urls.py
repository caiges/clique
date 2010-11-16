import os

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.index'),
    (r'^articles/(P<url>.*)$', 'core.views.article_show'),
    (r'^article-categories/$', 'core.views.article_categories_list'),
    (r'^article-categories/articles/$', 'core.views.articles_within_category'),
    (r'^article-categories/(?P<article_category_url>.*)/articles/(?P<article_url>.*)', 'core.views.article_within_category_show'),
    (r'^content-association/content_items.json', 'core.views.content_association'),
    (r'^content-association/content_items/remove.json', 'core.views.remove_content_association'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^pages/', include('external_apps.pages.urls')),
    (r'^product-categories/active$', 'core.views.active_product_categories_list'),
    (r'^product-categories$', 'core.views.product_categories_list'),
    (r'^product-categories/(?P<product_category_url>.*)/products/$', 'core.views.products_within_category'),
    (r'^product-categories/(?P<product_category_url>.*)/products/(?P<product_url>.*)', 'core.views.product_within_category_show'),
    (r'^product-categories/(?P<product_category_url>.*)/$', 'core.views.product_category_show'),
    (r'^products/(?P<product_id>\d+)/', 'core.views.product_show'),
    (r'^recipes/', include('external_apps.recipes.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/contentassocation/$', include('external_apps.contentassociation.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
