from django.db import models
from django.contrib.auth.models import User
from rest_framework.fields import CharField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    def get_context(self,request, *args, **kwargs):
        context   = super().get_context(request, *args, **kwargs)

        #chiamo tutti gli articoli e dopo lo meto nel paginator di 5 in 5.
        articoli = Articolo.objects.live().public().order_by('-first_published_at')
        paginator = Paginator(articoli, 5)
        
        page = request.GET.get("page")
        try:
            #Se la url dice ?page=x, ritorna la pagina x.
            posts = paginator.page(page)
        except PageNotAnInteger:
            #Se ?page=x, e x non è un numero
            posts = paginator.page(1)
        except EmptyPage:
            #Se non esis quella pagina.
            posts = paginator.page(paginator.num_pages)

        context['articoli'] = posts
        return context


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
            APIField('autore',serializer=CharField(source='autore.username')), #modificato con il serializer per ricevere solo il username
            APIField('data'),
            
    ]

    #parent page
    parent_page_types = ['blog.BlogHomePage']
