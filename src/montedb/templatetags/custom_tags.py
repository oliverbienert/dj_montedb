from django import template

register = template.Library()


@register.filter
def percentage(value):
    if value <= 0:
        return ""
    return format(value, ".0%")


@register.filter
def euro(value):
    if value == 0:
        return ""
    return format(value, ".2f").strip("0").strip(".") + " €"
