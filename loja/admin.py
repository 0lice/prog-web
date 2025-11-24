from django.contrib import admin

# Register your models here.

from .models import *

class FabricanteAdmin(admin.ModelAdmin):
    #cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria')
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'msgPromocao', 'categoria',)
    search_fields = ('Produto',)

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)
