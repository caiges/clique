import os

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^clique/', include('clique.foo.urls')),
    (r'^$', 'clique.core.views.index'),
    (r'^product-association/products.json/$', 'clique.core.views.product_association'),
    (r'^association-test/', 'clique.core.views.association_test'),
    (r'^products/', include('products.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
