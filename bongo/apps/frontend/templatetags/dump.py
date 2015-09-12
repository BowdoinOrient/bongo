from django import template

register = template.Library()


@register.filter(name='dump')
def dump(obj):
    return obj.__dict__
