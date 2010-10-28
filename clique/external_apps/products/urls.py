from django.conf.urls.defaults import *

urlpatterns = patterns('products.views',
    url(r'^$', 'product_index', name = 'product_index'),
    url(r'(?P<product_id>\d+)/$', 'product_show', name = 'product_show'),
)
