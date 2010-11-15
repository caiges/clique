from django import template

from clique.core.models import *

register = template.Library()

@register.tag
def get_product_navigation():
    product_categories = ProductCategory.objects.filter(product_categories__isnull = False).distinct()
    return product_categories
