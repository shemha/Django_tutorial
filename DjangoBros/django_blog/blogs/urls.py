# venv/lib/python3.8/site-package/django/urls/conf.pyの'path'変数
from django.urls import path
# アプリケーションディレクトリ'blogs'の'views.py'
from . import views

# アプリケーションディレクトリ名
app_name = 'blogs'
# 基準のURLの末尾に付与するパスを指定
urlpatterns = [
    # トップページのURLと読み込むviews.pyのindex関数を設定し、HTML内の代替名称を'index'に設定
    path('', views.index, name='index'),
    # 詳細ページのURL末尾はIDと対応させて生成、読み込むviews.pyのdetail関数を設定し、HTML内の代替名称を'detail'に設定
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    # 新規投稿ページのURLと読み込むviews.pyのnew関数を設定し、HTML内の代替名称を'new'に設定
    path('new/', views.new, name='new'),
    # 削除ページのURL末尾はIDと対応させて生成、読み込むviews.pyのdelete関数を設定し、HTML内の代替名称を'delete'に設定
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    # ページのURL末尾はIDと対応させて生成、読み込むviews.pyのedit関数を設定し、HTML内の代替名称を'edit'に設定
    path('edit/<int:blog_id>/', views.edit, name='edit'),
]