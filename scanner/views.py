from django.shortcuts import render
from django.db.models import Count, Sum
from .models import File

def home(request):
    """
    Главная страница с общей статистикой.

    Функция обрабатывает запрос на главную страницу и возвращает общую информацию
    о размерах файлов, сохраненных в базе данных.

    :param request: HTTP запрос
    :return: HTTP ответ с отрендеренным шаблоном home.html
    """
    """Главная страница с общей статистикой"""
    total_size_gb = File.objects.aggregate(total_size=Sum('size'))['total_size']
    total_size_gb = round(total_size_gb / (1024 ** 3), 2) if total_size_gb else 0  # Перевод в ГБ
    return render(request, 'scanner/home.html', {'total_size_gb': total_size_gb})

def file_statistics(request):
    """
    Отображает статистику файлов по их расширениям.

    Функция группирует файлы по расширению и считает количество файлов для каждого типа.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с отрендеренным шаблоном statistics.html.
    """
    file_stats = File.objects.values('extension').annotate(count=Count('id')).order_by('-count')
    return render(request, 'scanner/statistics.html', {'file_stats': file_stats})

def top_files(request):
    """
    Выводит список 10 самых больших файлов в системе.

    Функция сортирует файлы по размеру и выбирает 10 самых крупных.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с отрендеренным шаблоном top_files.html.
    """
    largest_files = File.objects.order_by('-size')[:10]
    return render(request, 'scanner/top_files.html', {'largest_files': largest_files})

def top_images(request):
    """
    Отображает 10 самых больших изображений.

    Функция фильтрует файлы по списку расширений, относящихся к изображениям, 
    и сортирует их по размеру.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с отрендеренным шаблоном top_images.html.
    """
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']
    largest_images = File.objects.filter(extension__in=image_extensions).order_by('-size')[:10]
    return render(request, 'scanner/top_images.html', {'largest_images': largest_images})

def top_documents(request):
    """
    Отображает 10 документов с наибольшим количеством страниц.

    Функция фильтрует файлы по списку расширений документов и выбирает 10 документов с 
    наибольшим количеством страниц.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с отрендеренным шаблоном top_documents.html.
    """
    documents = File.objects.filter(extension__in=['pdf', 'docx']).exclude(pages__isnull=True).order_by('-pages')[:10]
    return render(request, 'scanner/top_documents.html', {'largest_docs': documents})

def file_list(request):
    """
    Отображает полный список файлов.

    Функция извлекает все файлы из базы данных и передает их в шаблон.

    :param request: HTTP-запрос.
    :return: HTTP-ответ с отрендеренным шаблоном file_list.html.
    """
    files = File.objects.all()  # Получаем файлы
    return render(request, 'scanner/file_list.html', {'files': files})  # Передаем в шаблон

