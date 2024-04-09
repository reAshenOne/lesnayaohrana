from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your models here.

from modelcluster.fields import ParentalKey


from wagtail.models import Page,  Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.search import index

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class NewsIndexPage(Page):
    
    content_panels = Page.content_panels + [
        FieldPanel('title')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        newspages = self.get_children().live().order_by('-first_published_at')

        paginator = Paginator(newspages, 5)
        page = request.GET.get('page')

        try:
            newspages = paginator.page(page)
        except PageNotAnInteger:
            newspages = paginator.page(1)
        except EmptyPage:
            newspages = paginator.page(paginator.num_pages)

        context['newspages'] = newspages
        return context

class NewsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'NewsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class NewsPage(Page):
    date = models.DateTimeField("Post date")
    intro = models.CharField(max_length=500)
    body = RichTextField(blank=True)

    tags = ClusterTaggableManager(through=NewsPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

class NewsPageGalleryImage(Orderable):
    page = ParentalKey(NewsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class NewsTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        newspages = NewsPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['newspages'] = newspages
        return context

