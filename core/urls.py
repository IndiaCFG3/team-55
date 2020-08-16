from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display-chart', views.display_chart, name='display-chart'),
    path('chart', views.chart, name='chart'),
    path('upload-csv/', views.upload_csv, name='upload-csv'),
]