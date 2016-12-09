from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Information, Post, Gallery, Photo, Concept, Link, Quote
from django.utils.translation import get_language


class IndexView(TemplateView):
    template_name = 'girasol/concept.html'

    def get(self, request, *args, **kwargs):
        LANG = get_language()

        concept = None

        try:
            concept = Concept.objects.language(LANG).latest('date')
        except Concept.DoesNotExist:
            pass

        return render(request, self.template_name, {'concept': concept})


class PostView(DetailView):
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        LANG = get_language()

        self.queryset = Post.objects.language(LANG)

        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.object
        context['galleries'] = self.object.galleries.prefetch_related('photos')

        return context
