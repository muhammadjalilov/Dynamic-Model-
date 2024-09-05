from django.contrib import admin
from django.contrib.admin import TabularInline

from dynamic_forms.models import Form, Field


class FieldInline(TabularInline):
    model = Field
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['form_name', 'created_by', 'modified_at']
    list_filter = ['form_name', 'modified_at']
    inlines = [FieldInline,]


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'field_type', 'form']
