from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.urls import urlpatterns as product_urlpatterns

urlpatterns = [
    path('api/admin/', admin.site.urls),
    *product_urlpatterns,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
