from django.template.context_processors import request
from rest_framework import viewsets

from dynamic_forms.models import Form, Field, FormResponse
from dynamic_forms.serializers import FormSerializer, FieldSerializer, FormResponseSerializer


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return serializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class FormResponseViewSet(viewsets.ModelViewSet):
    queryset = FormResponse.objects.all()
    serializer_class = FormResponseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer
