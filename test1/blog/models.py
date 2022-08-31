from django.db import models
from modelcluster.fields import  ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


# The index Page
class BlogHomePage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro',classname='full')
    ]   

# articolo
class Articolo(Page):
    titolo      = models.CharField(max_length=250)
    descrizione = RichTextField()
    data        = models.DateField("data di publicazione")
    autore      = None #da importare tutta la classe User da django(very easy)
    copertina   = None #da fare il modelo image per la copertina 
    documento   = models.FileField(upload_to='uploads/% y/% m/% d/')
