from django.contrib import admin
from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('path', 'size', 'extension', 'width', 'height', 'pages')
    search_fields = ('path', 'extension')

