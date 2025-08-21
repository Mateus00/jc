from django.contrib import admin
from .models import Secao, Categoria, Galeria, Produto, Pagina

@admin.register(Secao)
class SecaoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    
@admin.register(Galeria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao',)
    search_fields = ('titulo',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'destaque')
    list_filter = ('categoria', 'destaque')
    search_fields = ('nome', 'descricao')
    
@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    list_filter = ('nome',)
    search_fields = ('nome',)
