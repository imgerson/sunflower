from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField

from parler.models import TranslatableModel, TranslatedFields

from datetime import datetime


class Photo(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Título", max_length=200),
        description = models.TextField("Descripción", blank=True, null=True),
    )
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(
        "Imagen", upload_to='imagenes/galerias', height_field='height',
        width_field='width')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['pk']
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"


class Gallery(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Título", max_length=200),
        description = models.TextField("Descripción", blank=True),
    )
    photos = models.ManyToManyField(Photo, blank=True)
    date = models.DateTimeField("Fecha", auto_now=True, blank=True)

    # Boolean fields
    slider = models.BooleanField("Slider", default=False)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Galería"
        verbose_name_plural = "Galerías"


class Quote(TranslatableModel):
    translations = TranslatedFields(
        quote = models.TextField("Frase")
    )
    author = models.CharField("Autor", max_length=200)

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self):
        return self.quote


class Link(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Título", max_length=200),
    )
    external_link = models.TextField()

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"

    def __str__(self):
        return self.title


class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Título", max_length=200),
        description = models.TextField("Descripción"),
        content = models.TextField("Contenido"),
    )
    author = models.CharField("Autor", max_length=200, default="")
    image = ImageField("Imagen", upload_to='imagenes/')
    date = models.DateTimeField(auto_now=True, blank=True)
    priority = models.PositiveIntegerField("Prioridad", blank=True, default=5)
    slug = models.SlugField(blank=True)
    quote = models.ForeignKey(Quote, null=True, blank=True)
    galleries = models.ManyToManyField(Gallery, blank=True)

    # Boolean Fields
    menu = models.BooleanField("Menú", default=True)
    navigation = models.BooleanField("Navegación", default=True)
    footer = models.BooleanField("Pie de página", default=True)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)


class Concept(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Título", max_length=200),
        description = models.TextField("Descripción"),
        content = models.TextField("Contenido"),
    )
    author = models.CharField("Autor", max_length=200)
    date = models.DateTimeField(auto_now=True, blank=True)
    gallery = models.ForeignKey(Gallery, null=True, blank=True)
    quote = models.ForeignKey(Quote, null=True, blank=True)

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    def __str__(self):
        return self.title


class Information(models.Model):
    contact = models.CharField("Correo ó Teléfono", max_length=200)

    email = models.BooleanField("Correo", default=False)
    phone = models.BooleanField("Teléfono", default=False)

    def __str__(self):
        return '{}'.format(self.contact)

    class Meta:
        verbose_name = "Información"
        verbose_name_plural = "Informaciones"
