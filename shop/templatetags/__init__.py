from django import template

register = template.Library()


@register.filter
def currency(value):
    try:
        return f'${value:,.2f}'
    except (TypeError, ValueError):
        return value
