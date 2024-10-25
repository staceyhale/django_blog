from blog.models import NetworkModel
from django import template

register = template.Library()


@register.inclusion_tag('blog/menu/networks.html')
def show_networks():
    networks = NetworkModel.objects.all()
    return {"networks": networks}

