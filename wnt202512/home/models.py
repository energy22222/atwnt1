from django.db import models
from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.fields import StreamField
from wnt202512.utils.blocks import StoryBlock, InternalLinkBlock
from wnt202512.utils.models import BasePage

from wnt202512.utils.blocks import BaseCardSectionBlock, CardSectionBlock 

 

class HomePage(BasePage):
    template = "pages/home_page.html"
    introduction = models.TextField(blank=True)
    hero_cta = StreamField(
        [("link", InternalLinkBlock())],
        blank=True,
        min_num=0,
        max_num=1,
    )
    body = StreamField(StoryBlock())
    featured_section_title = models.TextField(blank=True)

    # Au lieu de BaseCardSectionBlock() qui n'a pas de template : 
    carte = StreamField([   
        ("card_section", CardSectionBlock()), # Utilise la version avec template 
    ], use_json_field=True, blank=True) 
 

 
    search_fields = BasePage.search_fields +[
        index.SearchField("introduction"),
        index.SearchField("body"),
    ]

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("hero_cta"),
        FieldPanel("body"),
        FieldPanel("carte"),
        MultiFieldPanel(
            [
                FieldPanel("featured_section_title", heading="Title"),
                InlinePanel(
                    "page_related_pages",
                    label="Pages",
                    max_num=12,
                ),
            ],
            heading="Featured section",
        ),
    ]
