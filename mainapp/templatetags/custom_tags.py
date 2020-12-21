from django import template

register = template.Library()


@register.simple_tag
def xpleveling(level):
    return 5 * level * level - 5 * level+50


@register.simple_tag
def nameGenerator():
    return "a"