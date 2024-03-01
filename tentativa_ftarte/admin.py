from django.contrib import admin
from django.utils.html import format_html

from core.models import Clube


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'nome', 'ano_fundacao', 'divisao_atual','sexo', 'competicao', 'categoria', 'estado')

    def image_tag(self,time):
        return format_html(f'<img src="{time.image.url}" width="60"/>')
        image_tag.short_description = 'Image'
        list_display = ['name', 'image_tag']