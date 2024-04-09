from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    
    column1_title = models.CharField(max_length=255, blank=True)
    column1_text = RichTextField(blank=True)

    column2_title = models.CharField(max_length=255, blank=True)
    column2_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('column1_title'),
            FieldPanel('column1_text'),
            FieldPanel('column2_title'),
            FieldPanel('column2_text'),
        ], heading="Настройки страницы"),
    ]
