from django.shortcuts import render
from django.db.models import Count, Sum
from .models import File

def home(request):
    """Главная страница с общей статистикой"""
    total_size_gb = File.objects.aggregate(total_size=Sum('size'))['total_size']
    total_size_gb = round(total_size_gb / (1024 ** 3), 2) if total_size_gb else 0  # Перевод в ГБ
    return render(request, 'scanner/home.html', {'total_size_gb': total_size_gb})

def file_statistics(request):
    """Статистика файлов по расширениям"""
    file_stats = File.objects.values('extension').annotate(count=Count('id')).order_by('-count')
    return render(request, 'scanner/statistics.html', {'file_stats': file_stats})

def top_files(request):
    """Список топ-10 самых больших файлов"""
    largest_files = File.objects.order_by('-size')[:10]
    return render(request, 'scanner/top_files.html', {'largest_files': largest_files})

def top_images(request):
    """Список топ-10 самых больших изображений"""
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']
    largest_images = File.objects.filter(extension__in=image_extensions).order_by('-size')[:10]
    return render(request, 'scanner/top_images.html', {'largest_images': largest_images})

def top_documents(request):
    documents = File.objects.filter(extension__in=['pdf', 'docx']).exclude(pages__isnull=True).order_by('-pages')[:10]
    return render(request, 'scanner/top_documents.html', {'documents': documents})

