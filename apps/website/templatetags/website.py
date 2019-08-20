# -*- coding: utf-8 -*-
# @Filename : website
# @Date : 2019-08-20-00-50
# @Poject: wmc
# @AUTHOR : Christian Douglas <christian.douglas.alcantara@gmail.com>
from django.template.library import Library
from datetime import datetime

register = Library()


@register.filter(is_safe=False)
def date_from_ts(value, arg=None):
    """Format a date from timestamp."""
    if value in (None, ''):
        return ''
    try:
        return datetime.fromtimestamp(value)
    except AttributeError:
        try:
            return value
        except AttributeError:
            return ''

@register.simple_tag
def week_days_rain(value):
    days = [x['dt'] for x in value if x['humidity'] > 70]
    return days