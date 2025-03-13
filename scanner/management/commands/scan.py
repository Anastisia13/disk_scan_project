from django.core.management.base import BaseCommand
from scanner.utils import scan_directory

class Command(BaseCommand):
    help = 'Сканирует указанную директорию и сохраняет информацию о файлах в базе данных'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Путь к директории для сканирования')

    def handle(self, *args, **kwargs):
        directory = kwargs['directory']
        scan_directory(directory)
        self.stdout.write(self.style.SUCCESS(f'Сканирование завершено: {directory}'))

