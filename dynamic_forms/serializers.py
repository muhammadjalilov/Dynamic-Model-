from rest_framework import serializers

from dynamic_forms.models import Form, Field, FieldResponse, FormResponse


class FormSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    modified_at = serializers.ReadOnlyField()

    class Meta:
        model = Form
        fields = ['form_name', 'created_by', 'modified_at']


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class FieldResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldResponse
        fields = ['field', 'value']


class FormResponseSerializer(serializers.ModelSerializer):
    field_responses = FieldResponseSerializer(many=True)
    submitted_at = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = FormResponse
        fields = ['form', 'field_responses','submitted_at','user']

    def create(self, validated_data):
        field_responses_data = validated_data.pop('field_responses')
        form_response = FormResponse.objects.create(**validated_data)
        for field_response_data in field_responses_data:
            FieldResponse.objects.create(form_response=form_response, **field_response_data)
        return form_response
