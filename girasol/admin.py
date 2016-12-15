from django.contrib import admin

from parler.admin import TranslatableAdmin

from .models import Post, Information, Gallery, Photo, Link, Quote, Concept


class QuoteAdmin(TranslatableAdmin):
    list_display = ('quote',)
    fieldsets = ((None, {'fields': ('quote', 'author')}),)


class LinkAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = ((None, {'fields': ('title', 'external_link')}),)


class ConceptAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'description', 'content', 'author', 'gallery',
                'quote'),
        }),
    )


class PostAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'description', 'content', 'author', 'image',
                'galleries', 'quote', 'menu', 'navigation', 'footer',
                'priority'),
        }),
    )


class GalleryAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'photos', 'title', 'description', 'slider')
        }),
    )


class PhotoAdmin(TranslatableAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'description', 'image')
        }),
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Information)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Concept, ConceptAdmin)
