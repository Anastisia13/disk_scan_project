from django.urls import path
from . import views

"""
Маршруты (URL patterns) для приложения.

Определяет маршруты для различных страниц веб-приложения.

Доступные маршруты:
- 'files/' → Список всех файлов (file_list).
- '' → Главная страница с общей статистикой (home).
- 'statistics/' → Статистика файлов по расширениям (file_statistics).
- 'top-files/' → Топ-10 самых больших файлов (top_files).
- 'top-images/' → Топ-10 самых больших изображений (top_images).
- 'top-documents/' → Топ-10 документов с наибольшим количеством страниц (top_documents).
"""

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('', views.home, name='home'),
    path('statistics/', views.file_statistics, name='file_statistics'),
    path('top-files/', views.top_files, name='top_files'),
    path('top-images/', views.top_images, name='top_images'),
    path('top-documents/', views.top_documents, name='top_documents'),
]
