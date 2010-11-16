from django import template

from clique.core.models import *

register = template.Library()

class ProductNavigationNode(template.Node):
    def __init__(self, variable):
        product_categories = ProductCategory.objects.filter(products__isnull = False).distinct().order_by('name')
        print product_categories
        self.variable = variable
        self.product_categories = product_categories
    def render(self, context):
        context[self.variable] = self.product_categories
        return ''

@register.tag
def get_product_navigation(parser, token):
    """
    This will store a list of available product categories
    in the context.

    Usage::

        {% get_product_navigation as product_navigation %}
        {% for cat in product_navigation %}
        ...
        {% endfor %}

    This will pull the product categories from the database
    that contain products. It will leave out "empty" categories.
    """
    args = token.contents.split()
    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'get_product_navigation' requires 'as variable' (got %r)" % args)
    return ProductNavigationNode(args[2])
