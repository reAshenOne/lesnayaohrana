from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField

class StructurePage(Page):
    departments = ParentalManyToManyField('structure.Department', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('departments', widget=forms.CheckboxSelectMultiple),
    ]


@register_snippet
class Department(models.Model):
    name = models.CharField(max_length=255)
    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

@register_snippet  
class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='employees', null=True, blank=True,)
    photo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('full_name'),
        FieldPanel('position'),
        FieldPanel('department'),
        FieldPanel('photo'),
    ]

    def __str__(self):
        return self.full_name