from django.db import models
from django.contrib.auth.models import User

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body',classname="full"),
    ]
    subpage_types = ['blog.Articolo']

