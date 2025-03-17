from django.contrib import admin
from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """
    Конфигурация отображения модели File в административной панели Django.

    Отображает следующие поля:
    - name (Название файла)
    - path (Путь к файлу)
    - size (Размер файла)
    - extension (Расширение файла)
    """
    list_display = ('path', 'size', 'extension', 'width', 'height', 'pages')
    search_fields = ('path', 'extension')

