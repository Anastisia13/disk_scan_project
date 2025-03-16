from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('', views.home, name='home'),
    path('statistics/', views.file_statistics, name='file_statistics'),
    path('top-files/', views.top_files, name='top_files'),
    path('top-images/', views.top_images, name='top_images'),
    path('top-documents/', views.top_documents, name='top_documents'),
]

