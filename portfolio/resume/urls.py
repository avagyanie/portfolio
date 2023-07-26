from .views import home, portfolio_project
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('portfolio_project/<int:id>', portfolio_project, name='portfolio_project'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

