from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormViewSet, FieldViewSet, FormResponseViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'form-responses', FormResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
