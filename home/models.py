from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField


from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailvideos.blocks import VideoChooserBlock

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel


NULLABLE = {'null': True, 'blank': True}


class HomePage(Page):

    class Meta:
        verbose_name = 'Flaming stove'
    body = StreamField([
        ('description', blocks.StructBlock([
            ('text', blocks.RichTextBlock(**NULLABLE, required=False)),
            ('image', ImageChooserBlock(**NULLABLE, required=False, label='Картинка')),
            ('svg', SvgChooserBlock(**NULLABLE, required=False, label='Логотип')),

        ]))
    ], **NULLABLE)

    content_panels = Page.content_panels +[
        StreamFieldPanel('body'),
    ]


    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['privilege'] = Privilege.objects.all()
        return context


class Privilege(Page):
    class Meta:
        verbose_name = 'Преимущества'

    page_title = models.CharField(max_length=150, **NULLABLE, verbose_name='Заголовок')
    body = StreamField([
        ('description', blocks.StructBlock([
            ('text', blocks.RichTextBlock(**NULLABLE, required=False, label='Текст')),
            ('image', ImageChooserBlock(**NULLABLE, required=False, label='Картинка')),
            ], label='Преимущество'))
    ], **NULLABLE, verbose_name='Блок преимуществ')

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        StreamFieldPanel('body'),
    ]
