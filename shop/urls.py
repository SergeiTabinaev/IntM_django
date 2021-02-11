from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls  # Автодокументирование


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # регистрация авторизация
    path('auth/', include('djoser.urls.authtoken')),  # регистрация авторизация (токены сохраняются в БД)

    path('product-specs/', include('specs.urls')),
    path('api/', include('mainapp.api.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
