from django import template

register = template.Library()
@register.filter(name='get_values')
def get_values(dict,key):
    print(dict.get(key))
    # return dict.get(key)
