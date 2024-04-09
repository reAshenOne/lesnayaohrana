from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField
from wagtail.fields import RichTextField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class VacanciesIndexPage(Page):
    
    def get_context(self, request):
        context = super().get_context(request)
        vacanciespages = self.get_children().live().order_by('-first_published_at')

        paginator = Paginator(vacanciespages, 5)
        page = request.GET.get('page')

        try:
            vacanciespages = paginator.page(page)
        except PageNotAnInteger:
            vacanciespages = paginator.page(1)
        except EmptyPage:
            vacanciespages = paginator.page(paginator.num_pages)

        context['vacanciespages'] = vacanciespages
        return context

class VacanciesPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
