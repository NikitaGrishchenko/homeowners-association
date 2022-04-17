from django import template
from django.db.models import Q

from ..models import Gallery

register = template.Library()


@register.inclusion_tag("components/gallery.html")
def gallery() -> dict:
    first_object = Gallery.objects.latest('date')
    objects = Gallery.objects.filter(~Q(id=first_object.id))
    return {
        "images": objects,
        "first_image": first_object,
    }

