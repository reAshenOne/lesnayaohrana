from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField
from wagtail.fields import RichTextField

class ContactsPage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]