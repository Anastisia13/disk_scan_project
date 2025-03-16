from django.test import TestCase
from scanner.models import File
from scanner.utils import scan_directory
import os

class FileModelTest(TestCase):
    """Тесты для модели File"""

    def setUp(self):
        """Создаем тестовые файлы"""
        self.test_file = File.objects.create(
            path='/test/path/file.pdf',
            size=1024,
            extension='pdf',
            width=None,
            height=None,
            pages=10
        )

    def test_file_creation(self):
        """Проверяем, что объект File был успешно создан"""
        self.assertEqual(self.test_file.path, '/test/path/file.pdf')
        self.assertEqual(self.test_file.size, 1024)
        self.assertEqual(self.test_file.extension, 'pdf')
        self.assertEqual(self.test_file.pages, 10)

    def test_file_str_representation(self):
        """Проверяем строковое представление объекта File"""
        self.assertEqual(str(self.test_file), '/test/path/file.pdf')

class ScanDirectoryTest(TestCase):
    """Тесты для функции scan_directory"""

    def setUp(self):
        """Создаем временную папку с файлами"""
        self.test_dir = 'test_scan_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'test.pdf'), 'w') as f:
            f.write('%PDF-1.4')

    def test_scan_directory(self):
        """Проверяем, что сканирование директории работает"""
        scan_directory(self.test_dir)
        scanned_files = File.objects.filter(path__contains='test.pdf')
        self.assertEqual(scanned_files.count(), 1)

    def tearDown(self):
        """Удаляем тестовую папку"""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

