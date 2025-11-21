from django.contrib import admin
from .models import Comentarios, Posts

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'categoria', 'conteudo', 'data')

admin.site.register(Comentarios)
