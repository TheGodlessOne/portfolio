from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_all, name='projects'),
    path('<int:p_key>/', views.project_detail, name='project_detail'),
]
