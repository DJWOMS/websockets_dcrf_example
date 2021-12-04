from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('room/<int:pk>/', views.room, name='room'),
    path('', views.index, name='index'),
]
