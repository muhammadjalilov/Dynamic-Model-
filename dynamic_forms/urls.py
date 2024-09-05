from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormViewSet, FieldViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'fields', FieldViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
