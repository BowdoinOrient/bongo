from django import template

register = template.Library()

@register.filter(name='class_name')
def class_name(value):
    return value.__class__.__name__