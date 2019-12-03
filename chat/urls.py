from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.chats_list, name='chats_list'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    path(r'^<name_chat>/', views.masege_ls, name='masege_ls'),
]