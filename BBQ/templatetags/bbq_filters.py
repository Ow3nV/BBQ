from django import template
from bbqweb.models import Barbeque

register = template.Library()


@register.filter
def get_bbq_image_url(bbq_id):
    bbq = Barbeque.objects.get(id=bbq_id)
    return bbq.image.url

