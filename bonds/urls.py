from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BondViewSet


router = DefaultRouter()
router.register(r'bonds', BondViewSet, basename='bond')

urlpatterns = [
    path('', include(router.urls))
]
