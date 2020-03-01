from django.urls import path

from . import views

urlpatterns = [
    path('index/', index, name='index')
]
