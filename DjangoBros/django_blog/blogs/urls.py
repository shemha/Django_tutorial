# 新しくファイルを作成しました
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),  # ブログ管理ページ
    path('detail/<int:blog_id>/', views.detail, name='detail'),  # 詳細ページ
    path('new/', views.new, name='new'),  # 新規ブログ記事投稿ページ
    path('delete/<int:blog_id>/', views.delete, name='delete'),  # Delete機能
]