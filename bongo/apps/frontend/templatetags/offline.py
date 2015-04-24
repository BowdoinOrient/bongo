from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='offline')
def offline(value):
    return settings.OFFLINE
