from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('projects/', views.project_all, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
