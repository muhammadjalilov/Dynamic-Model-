from django.contrib.auth.models import User
from django.db import models


class Form(models.Model):
    form_name = models.CharField(max_length=256, verbose_name='Form Name')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forms', verbose_name='CreatedBy')
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.form_name

    class Meta:
        ordering = ['-modified_at']


class Field(models.Model):
    FIELD_TYPES = (
        ('int', 'Integer'),
        ('str', 'String'),
        ('bool', 'Boolean')
    )
    name = models.CharField(max_length=256, verbose_name='Field Name')
    field_type = models.CharField(max_length=4, choices=FIELD_TYPES, verbose_name='Field Type')
    form = models.ForeignKey(Form, related_name='fields', on_delete=models.CASCADE, verbose_name='Form')

    def __str__(self):
        return self.name
