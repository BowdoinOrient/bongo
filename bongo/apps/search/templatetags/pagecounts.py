from django import template

register = template.Library()

@register.filter(name='count')
def count(page):
    return page.paginator._count
    # return len([obj for obj in page.object_list if obj is not None])

@register.filter(name='firstindex')
def firstindex(page):
    return (page.number - 1) * page.paginator.per_page + 1

@register.filter(name='lastindex')
def lastindex(page):
    return page.number * min(page.paginator.per_page, count(page))

@register.filter(name='has_previous')
def has_previous(page):
    return page.has_previous

@register.filter(name='has_next')
def has_next(page):
    if page.has_next and page.page_objects[page.paginator.per_page] is not None:
        return True
    return False