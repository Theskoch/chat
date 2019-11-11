from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats_list, name='chats_list'),
    path('<str:name>/', views.masege_ls, name='masege_ls'),
]