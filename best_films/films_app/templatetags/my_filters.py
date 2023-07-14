from django import template

register = template.Library()


@register.filter
def last_elem(path):
    return path.split('/')[-2]
