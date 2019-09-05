from rest_framework.routers import DefaultRouter

from product.views import ProductViewset


router = DefaultRouter()
router.register(r'api/v1/products', ProductViewset, basename='products')

urlpatterns = [
    *router.urls
]