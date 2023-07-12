from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', home, name='home'), # new
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
