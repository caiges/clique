from django import template

register = template.Library()

@register.filter
def class_name_lookup(instance):
    return instance.__class__.__name__.lower()
