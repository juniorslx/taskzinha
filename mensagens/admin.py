from django.contrib import admin
from .models import Mensagens

@admin.register(Mensagens)
class MensagensAdmin(admin.ModelAdmin):
    list_display = ('nome', 'texto', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'texto')
