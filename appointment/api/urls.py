from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AppointmentsViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
