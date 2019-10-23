from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats_list, name='chats_list'),
]