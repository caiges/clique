from django import template

register = template.Library()

@register.filter
def class_name_lookup(instance):
        if(instance.__class__.__name__.lower() == 'str'):
            return ''
        else:
            return instance.__class__.__name__.lower()
