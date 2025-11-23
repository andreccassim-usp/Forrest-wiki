from django.contrib import admin
from .models import Posts, Categoria, Comentarios


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


class ComentariosInline(admin.TabularInline):
    model = Comentarios
    extra = 0


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("name", "data")
    search_fields = ("name", "conteudo")
    list_filter = ("categorias", )
    filter_horizontal = ("categorias",)  # interface para escolher categorias
    inlines = [ComentariosInline]


@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "likes", "post")
    search_fields = ("text", "author__username")
