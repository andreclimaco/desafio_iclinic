from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChargesViewSet

router = DefaultRouter()
router.register(r'charges', ChargesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
