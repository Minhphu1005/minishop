from django import template
register = template.Library()
@register.inclusion_tag('cart/quantity_select.html')
def quantity_select(item):
    return {'item': item}