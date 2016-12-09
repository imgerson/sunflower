from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

from .views import IndexView, PostView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'(?P<slug>[\w-]+)/$', PostView.as_view(), name='post-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
