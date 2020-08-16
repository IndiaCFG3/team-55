from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-csv/', views.upload_csv, name='upload-csv'),
]