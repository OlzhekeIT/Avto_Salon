from django import template

register = template.Library()

@register.filter(name='kzt_format')
def kzt_format(value):
    try:
        value = int(value)
        return "{:,.0f} ₸".format(value).replace(',', ' ')
    except (ValueError, TypeError):
        return value
