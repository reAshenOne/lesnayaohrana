from django.db import models
from wagtail.documents.models import Document
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class DocumentsIndexPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('document_items', label="Documents"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        
        search_query = request.GET.get('q')
        documents = self.document_items.all()

        if search_query:
            documents = documents.filter(
                Q(document_title__icontains=search_query)
            )

        
        paginator = Paginator(documents, 10)  
        page_number = request.GET.get('page')

        try:
            documents = paginator.page(page_number)
        except PageNotAnInteger:
            documents = paginator.page(1)
        except EmptyPage:
            documents = paginator.page(paginator.num_pages)

        context['documents'] = documents
        return context

class DocumentItem(Orderable):
    page = ParentalKey(DocumentsIndexPage, on_delete=models.CASCADE, related_name='document_items')
    document = models.ForeignKey(
        Document,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    document_title = models.CharField(max_length=250)


    panels = [
        FieldPanel('document_title'),
        FieldPanel('document'),
    ]
