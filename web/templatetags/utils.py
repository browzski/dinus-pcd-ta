from django import template
register = template.Library()

@register.filter
def createActive( href, active):
    if(active == href):
       cls = "link-secondary" 
    else:
       cls = "link-dark"

    return cls
    