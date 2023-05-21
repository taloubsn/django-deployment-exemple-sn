from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, args):
    """
        This cut all values
    """
    return value.replace(args, '')

# register.filter('cut', cut)