from rest_framework import serializers

from dynamic_forms.models import Form, Field


class FormSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    modified_at = serializers.ReadOnlyField()
    class Meta:
        model = Form
        fields = ['form_name','created_by','modified_at']

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'