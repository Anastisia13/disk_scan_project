import os
from django.db import models

class File(models.Model):
    """
    Модель для представления файла в системе.

    Эта модель хранит информацию о файле, включая имя, размер и путь к файлу.

    Атрибуты:
        name (CharField): Название файла. Может быть пустым.
        path (CharField): Полный путь к файлу в файловой системе.
        size (BigIntegerField): Размер файла в байтах.
        extension (CharField): Расширение файла (например, 'jpg', 'pdf').
        width (IntegerField): Ширина изображения (если применимо). Может быть пустым.
        height (IntegerField): Высота изображения (если применимо). Может быть пустым.
        pages (IntegerField): Количество страниц в документе (например, PDF). Может быть пустым.
    """
    name = models.CharField(max_length=256, blank=True, null=True)
    path = models.CharField(max_length=1024)  # Путь к файлу
    size = models.BigIntegerField()  # Размер файла в байтах
    extension = models.CharField(max_length=10)  # Расширение файла
    width = models.IntegerField(null=True, blank=True)  # Ширина изображения
    height = models.IntegerField(null=True, blank=True)  # Высота изображения
    pages = models.IntegerField(null=True, blank=True)  # Количество страниц (например, в PDF)

    def save(self, *args, **kwargs):
        """
        Возвращает строковое представление объекта File, которое будет показывать его название.

        :return: Название файла.
        """
        # Если имя файла не задано, извлекаем его из пути
        if not self.name:
            self.name = os.path.basename(self.path)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращает строковое представление объекта File.

        :return: Название файла, если оно задано, иначе путь к файлу.
        """
        return self.name if self.name else self.path
    
    # Новый метод для получения размера файла
    def calculate_size(self):
        """
        Функция для получения размера файла.
        """
        return self.size

    # Метод для проверки, является ли файл изображением
    def is_image(self):
        """
        Проверка, является ли файл изображением.
        """
        return self.extension.lower() in ['jpg', 'jpeg', 'png', 'gif']

    # Метод для проверки, является ли файл документом
    def is_document(self):
        """
        Проверка, является ли файл документом.
        """
        return self.extension.lower() in ['pdf', 'docx', 'txt']

    # Метод для проверки, является ли файл большим (больше 5MB)
    def is_large(self):
        """
        Проверка, является ли файл большим (больше 5MB).
        """
        return self.size > 5 * 1024 * 1024  # 5MB

