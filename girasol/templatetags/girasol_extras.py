from django import template
from django.utils.translation import get_language, get_language_from_request

from girasol.models import Post, Information, Gallery, Photo, Quote, Link


register = template.Library()


@register.inclusion_tag('girasol/menu.html')
def show_main_menu():
    LANG = get_language()

    links = Post.objects.language(LANG).filter(menu=True)

    return {'links': links}

@register.inclusion_tag('girasol/navigation.html')
def show_navigation():
    LANG = get_language()

    links = Post.objects.language(LANG).filter(navigation=True)

    return {'links': links}

@register.inclusion_tag('girasol/footer.html')
def show_footer():
    LANG = get_language()

    links = Post.objects.language(LANG).filter(footer=True)

    return {'links': links}

@register.inclusion_tag('girasol/footer_sec.html')
def show_footer_sec():
    LANG = get_language()

    links = Link.objects.language(LANG).all()

    return {'links': links}


@register.inclusion_tag('girasol/emails.html')
def show_email_addresses():
    emails = Information.objects.filter(email=True)

    return {'emails': emails}

@register.inclusion_tag('girasol/phones.html')
def show_phone_numbers():
    phones = Information.objects.filter(phone=True)

    return {'phones': phones}

@register.inclusion_tag('girasol/slider.html')
def show_slider():
    LANG = get_language()

    gallery = Gallery.objects.language(LANG)
    gallery = gallery.filter(slider=True)
    gallery = gallery.prefetch_related('photos').order_by('-date')[0]

    return {'gallery': gallery}
