# scanner/tests.py
from django.test import TestCase
from scanner.models import File

class FileModelTests(TestCase):

    def test_file_creation(self):
        """Тестирование создания объекта File"""
        # Создаем объект без указания name, он будет установлен автоматически
        file = File.objects.create(
            path="/path/to/file1.txt",
            size=1024,
            extension="txt"
        )
    
        # Проверяем, что имя файла правильно установлено (оно должно быть извлечено из пути)
        self.assertEqual(file.name, "file1.txt")
    
        # Проверяем другие поля
        self.assertEqual(file.size, 1024)
        self.assertEqual(file.extension, "txt")
    
        # Проверяем строковое представление объекта (оно должно быть равно имени файла)
        self.assertEqual(str(file), "file1.txt")


    def test_missing_name_field(self):
        """Тестирование создания объекта File без имени. Имя должно быть извлечено из пути"""
        file = File.objects.create(
            path="/path/to/file2.txt",
            size=2048,
            extension="txt"
        )
        self.assertEqual(file.name, "file2.txt")

    def test_invalid_path(self):
        """Тестирование создания объекта File с неправильным путем"""
        file = File.objects.create(
            path="not/a/valid/path.txt",
            size=512,
            extension="txt",
            name="invalid.txt"
        )
        self.assertEqual(file.name, "invalid.txt")
    
    def test_file_size(self):
        """
        Тестируем правильность хранения размера файла.
        """
        file = File.objects.create(
            path="/path/to/file3.txt",
            size=4096,
            extension="txt"
        )
        self.assertEqual(file.size, 4096)

    def test_file_extension(self):
        """
        Тестируем правильность хранения расширения файла.
        """
        file = File.objects.create(
            path="/path/to/file4.jpeg",
            size=2048,
            extension="jpeg"
        )
        self.assertEqual(file.extension, "jpeg")

    def test_file_name_method(self):
        """
        Тестируем метод __str__ модели File.
        """
        file = File.objects.create(
            path="/path/to/file5.docx",
            size=1024,
            extension="docx"
        )
        self.assertEqual(str(file), "file5.docx")

    def test_file_with_empty_name(self):
        """
        Тестируем создание объекта File с пустым именем.
        """
        file = File.objects.create(
            path="/path/to/emptyfile.txt",
            size=0,
            extension="txt"
        )
        self.assertEqual(file.name, "emptyfile.txt")


# scanner/tests.py
from django.test import TestCase
from django.urls import reverse
from scanner.models import File

class FileViewsTests(TestCase):

    def setUp(self):
        """Создание файлов для тестов"""
        File.objects.create(
            path="/path/to/file1.txt",
            size=1024,
            extension="txt",
            name="file1.txt"
        )
        File.objects.create(
            path="/path/to/file2.jpg",
            size=2048,
            extension="jpg",
            name="file2.jpg"
        )


    def test_home_view(self):
        """Тестирование главной страницы"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Добро пожаловать в проект сканирования жесткого диска!")

    def test_invalid_url(self):
        """Тестирование неправильного URL"""
        response = self.client.get('/invalid-url/')
        self.assertEqual(response.status_code, 404)

 
    def test_404_error_page(self):
        """
        Тестируем обработку 404 ошибки.
        """
        response = self.client.get('/non-existing-url/')
        self.assertEqual(response.status_code, 404)

    
class FileUtilsTests(TestCase):

    def test_calculate_file_size(self):
        """
        Тестируем функцию для вычисления размера файла.
        """
        file = File.objects.create(
            path="/path/to/file8.txt",
            size=12345,
            extension="txt"
        )
        self.assertEqual(file.calculate_size(), 12345)

    def test_is_image_file(self):
        """
        Тестируем функцию для проверки, является ли файл изображением.
        """
        file = File.objects.create(
            path="/path/to/image.jpg",
            size=2000,
            extension="jpg"
        )
        self.assertTrue(file.is_image())
        
    def test_is_document_file(self):
        """
        Тестируем функцию для проверки, является ли файл документом.
        """
        file = File.objects.create(
            path="/path/to/document.pdf",
            size=4000,
            extension="pdf"
        )
        self.assertTrue(file.is_document())

    def test_is_large_file(self):
        """
        Тестируем функцию для проверки, является ли файл большим.
        """
        file = File.objects.create(
            path="/path/to/largefile.txt",
            size=10000000,
            extension="txt"
        )
        self.assertTrue(file.is_large())

from django.test import TestCase
from scanner.models import File

class FileModelTests(TestCase):

    def test_file_creation(self):
        """Тестирование создания файла и его методов"""
        # Создаем файл
        file = File.objects.create(
            path="/test/path/file1.txt",
            size=1024,
            extension="txt",
            name="file1.txt"
        )
        
        # Проверяем создание объекта
        self.assertEqual(file.name, "file1.txt")
        self.assertEqual(file.size, 1024)
        self.assertEqual(file.extension, "txt")
        
        # Проверяем метод для получения размера файла
        self.assertEqual(file.calculate_size(), 1024)
        
        # Проверяем методы для проверки типа файла
        self.assertTrue(file.is_document())  # Для файла .txt должно вернуть True
        self.assertFalse(file.is_image())  # Для файла .txt должно вернуть False
        
        # Проверяем, является ли файл большим (должно вернуть False, т.к. размер < 5MB)
        self.assertFalse(file.is_large())
        
        # Теперь создадим файл больше 5MB и проверим его
        large_file = File.objects.create(
            path="/test/path/large_file.jpg",
            size=10 * 1024 * 1024,  # 10MB
            extension="jpg",
            name="large_file.jpg"
        )
        
        # Проверяем, что это большой файл
        self.assertTrue(large_file.is_large())  # Для файла размером 10MB должно вернуть True

from django.test import TestCase
from scanner.models import File

class FileModelTests(TestCase):

    def test_file_creation_empty_fields(self):
        """Тестирование создания файла с пустыми полями"""
        file = File.objects.create(path="/path/to/file2.txt", size=2048, extension="txt")
        self.assertEqual(file.name, "file2.txt")
        self.assertEqual(file.size, 2048)
        self.assertEqual(file.extension, "txt")

    def test_file_size(self):
        """Тестируем метод для получения размера файла"""
        file = File.objects.create(path="/path/to/file3.txt", size=1024, extension="txt")
        self.assertEqual(file.calculate_size(), 1024)

    def test_is_image(self):
        """Тестируем метод, который проверяет, является ли файл изображением"""
        file = File.objects.create(path="/path/to/image.jpg", size=2048, extension="jpg")
        self.assertTrue(file.is_image())

    def test_is_document(self):
        """Тестируем метод, который проверяет, является ли файл документом"""
        file = File.objects.create(path="/path/to/document.pdf", size=2048, extension="pdf")
        self.assertTrue(file.is_document())

    def test_is_large(self):
        """Тестируем метод для проверки, является ли файл большим"""
        file = File.objects.create(path="/path/to/largefile.mp4", size=6 * 1024 * 1024, extension="mp4")
        self.assertTrue(file.is_large())

    def test_file_name_from_path(self):
        """Тест на извлечение имени файла из пути"""
        file = File.objects.create(path="/path/to/file5.txt", size=1024, extension="txt")
        self.assertEqual(file.name, "file5.txt")

    def test_empty_file_size(self):
        """Тест на добавление файла с нулевым размером"""
        file = File.objects.create(path="/path/to/emptyfile.txt", size=0, extension="txt")
        self.assertEqual(file.size, 0)

    def test_multiple_files_creation(self):
        """Тест на создание нескольких файлов"""
        file1 = File.objects.create(path="/path/to/file9.txt", size=1024, extension="txt")
        file2 = File.objects.create(path="/path/to/file10.jpg", size=2048, extension="jpg")
        self.assertEqual(File.objects.count(), 2)

    def test_path_with_spaces(self):
        """Тест на путь с пробелами"""
        file = File.objects.create(path="/path/to/file with spaces.txt", size=1024, extension="txt")
        self.assertTrue(file.path)

    def test_file_creation_without_name(self):
        """Тест на создание файла без имени, имя извлекается из пути"""
        file = File.objects.create(path="/path/to/file11.txt", size=1024, extension="txt")
        self.assertEqual(file.name, "file11.txt")

    def test_file_with_invalid_extension(self):
        """Тест на создание файла с неверным расширением"""
        file = File.objects.create(path="/path/to/file12.xyz", size=1024, extension="xyz")
        self.assertEqual(file.extension, "xyz")

    def test_file_creation_with_large_size(self):
        """Тест на создание файла с размером больше 5MB"""
        file = File.objects.create(path="/path/to/largefile13.txt", size=10 * 1024 * 1024, extension="txt")
        self.assertTrue(file.is_large())

