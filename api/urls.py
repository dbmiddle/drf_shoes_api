from django.conf.urls import include, url

from api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeColorViewSet, ShoeViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')
router.register(r'shoetype', ShoeTypeViewSet, basename='shoetype')
router.register(r'shoecolor', ShoeColorViewSet, basename='shoecolor')
router.register(r'shoe', ShoeViewSet, basename='shoe')

urlpatterns = [
    url(r'', include(router.urls))
]
