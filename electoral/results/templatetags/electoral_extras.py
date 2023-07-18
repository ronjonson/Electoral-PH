from django import template

register = template.Library()

@register.filter(name="lookup")
def lookup(d,key):
    try:
        return d[key]
    except:
        print(f'error at {d} with {key}')
