from django.db import models

class File(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True) 
    path = models.CharField(max_length=1024)  # Путь к файлу
    size = models.BigIntegerField()  # Размер файла в байтах
    extension = models.CharField(max_length=10)  # Расширение файла
    width = models.IntegerField(null=True, blank=True)  # Ширина изображения
    height = models.IntegerField(null=True, blank=True)  # Высота изображения
    pages = models.IntegerField(null=True, blank=True)  # Количество страниц (например, в PDF)

    def save(self, *args, **kwargs):
        # Если имя файла не задано, извлекаем его из пути
        if not self.name:
            self.name = os.path.basename(self.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.path 
