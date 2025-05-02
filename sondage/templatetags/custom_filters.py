from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def dict_get(d, key):
    try:
        return d.get(key)
    except (AttributeError, TypeError):
        return ''
