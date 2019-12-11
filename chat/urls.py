from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.chats_list, name='chats_list'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^test_chat/',views.chat_test_class.chats_test,name='test_chat'),
    url(r'^test_json/', views.test_json_fanck, name='test_json'),
    path(r'^<name_chat>/', views.masege_ls, name='masege_ls'),
]