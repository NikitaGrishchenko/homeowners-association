from django import template
from django.db.models import Q

from ..models import Advertising, Gallery, News

register = template.Library()


@register.inclusion_tag("components/gallery.html")
def gallery() -> dict:
    first_object = Gallery.objects.latest('date')
    objects = Gallery.objects.filter(~Q(id=first_object.id))

    return {
        "images": objects,
        "first_image": first_object,
    }

@register.inclusion_tag("components/basic-information-last-news.html")
def basic_information_last_news() -> dict:
    latest_five_advertising = Advertising.objects.all().order_by("-id")[:5]
    latest_five_news = News.objects.all().order_by("-id")[:5]

    return {
        "ads": latest_five_advertising,
        "news": latest_five_news,
    }
