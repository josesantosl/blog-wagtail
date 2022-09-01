from django.db import models
from django.contrib.auth.models import User
from modelcluster.fields import  ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.api import APIField


# The index Page
class BlogHomePage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro',classname='full')
    ]   

    subpage_types = ['blog.Articolo']

# articolo
class Articolo(Page):
    #variabili dell'articolo
    descrizione = RichTextField()
    testo       = RichTextField()
    data        = models.DateField("data di publicazione")
    autore      = models.ForeignKey(User,default=0, on_delete=models.PROTECT)

    #per la copertina provo di usare il sistema delle imagini di waigtail
    copertina= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    documento   = models.FileField(upload_to='uploads/% y/% m/% d/',blank=True)

    #searchfields
    search_fields = Page.search_fields + [
            index.SearchField('title'),
            index.SearchField('autore'),
    ]

    # the fields to create a new article.
    content_panels = Page.content_panels + [
            FieldPanel('descrizione'),
            FieldPanel('testo'),
            FieldPanel('autore'),
            FieldPanel('data'),
            FieldPanel('copertina'),
            FieldPanel('documento'),
    ]

    # fields to export over the api.
    api_fields = [
            APIField('title'),
            APIField('descrizione'),
            APIField('testo'),
            APIField('autore'),
            APIField('data'),
            
    ]

    #parent page
    parent_page_types = ['blog.BlogHomePage']
