# your_app/templatetags/your_custom_tags.py
from django import template

register = template.Library()

@register.filter(name='my_tags')
def get_item(list, index):
    try:
        return list[index]
    except:
        return ''