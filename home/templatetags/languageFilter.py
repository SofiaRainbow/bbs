from django.template import Library

register = Library()


@register.filter
def concat(value, value2):
    return value + '_'+value2
