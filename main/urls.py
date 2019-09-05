import os

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.template import Template, Context
import torch

from medindex.urls import urlpatterns as medindex_urlpatterns
from nlp_processor.urls import urlpatterns as reports_urlpatterns


def test_cuda(request):
    cuda_available = torch.cuda.is_available()
    t = Template(f'cuda is available: {cuda_available}; env: {os.environ["GMAIL_USER"]}')
    html = t.render(Context({}))

    return HttpResponse(html)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/test-cuda/', test_cuda, name='test_cuda'),
    *medindex_urlpatterns,
    *reports_urlpatterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
