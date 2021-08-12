# 新規作成ファイル
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),  # トップページのurl
    path('users/<int:pk>/', views.users_detail, name='users_detail'),  # ユーザーページのurl
]