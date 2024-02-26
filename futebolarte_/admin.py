from django.contrib import admin
from core.models import Clube


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'cores', 'ano_fundacao', 'tem_mundial')
    list_filter = ('estado', 'ano_fundacao', 'tem_mundial')
    search_fields = ('nome', 'estado')
