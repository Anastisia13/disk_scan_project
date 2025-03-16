import os
import logging
from scanner.models import File
from PIL import Image
from PyPDF2 import PdfReader

# Настроим логирование
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Выводим в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def scan_directory(directory):
    """
    Сканирует указанную директорию, извлекает информацию о файлах и сохраняет в базу данных.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_ext = os.path.splitext(file)[1].lower().strip('.')
            file_name = os.path.basename(file_path)

            width = height = pages = None

            logger.info(f"Обрабатывается файл: {file_path}, размер: {file_size} байт")


            if file_ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        logger.info(f"Изображение: {file_path}, ширина: {width}, высота: {height}")           
                except Exception as e:
                    logger.error(f"Ошибка при обработке изображения {file_path}: {e}")

            elif file_ext == 'pdf':
                try:
                    with open(file_path, "rb") as pdf_file:
                        pdf_reader = PdfReader(pdf_file)
                        pages = len(pdf_reader.pages)
                        logger.info(f"PDF: {file_path}, страниц: {pages}")               
                except Exception as e:
                    logger.error(f"Ошибка при обработке PDF {file_path}: {e}")

            try:
                File.objects.create(
                    name=file_name,
                    path=file_path,
                    size=file_size,
                    extension=file_ext,
                    width=width,
                    height=height,
                    pages=pages
                )
                logger.info(f"Данные о файле {file_path} успешно сохранены в базу данных.")
            except Exception as e:
                logger.error(f"Ошибка при сохранении данных файла {file_path} в базу данных: {e}")
