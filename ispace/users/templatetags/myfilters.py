from datetime import timedelta

from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(value, arg):
    return value.as_widget(attrs={"class": arg})


@register.filter(name="check_edited")
def check_edited(value, arg):
    if value < arg - timedelta(minutes=1):
        return True
