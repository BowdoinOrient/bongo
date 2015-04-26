from django import template

register = template.Library()

@register.filter(name='count')
def count(page):
    return page.paginator._count

@register.filter(name='firstindex')
def firstindex(page):
    return (page.number - 1) * page.paginator.per_page + 1

@register.filter(name='lastindex')
def lastindex(page):
    return page.number * min(page.paginator.per_page, count(page))