from django.db import models

class File(models.Model):
    path = models.CharField(max_length=1024)  # Путь к файлу
    size = models.BigIntegerField()  # Размер файла в байтах
    extension = models.CharField(max_length=10)  # Расширение файла
    width = models.IntegerField(null=True, blank=True)  # Ширина изображения
    height = models.IntegerField(null=True, blank=True)  # Высота изображения
    pages = models.IntegerField(null=True, blank=True)  # Количество страниц (например, в PDF)

    def __str__(self):
        return self.path

