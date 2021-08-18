"""ecsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# venv/lib/python3.8/site-packages/django/contrib/adminディレクトリ
from django.contrib import admin
# venv/lib/python3.8/site-packages/django/url/conf.pyの'path'変数と'include'メソッド
from django.urls import path, include  # 'include'追加
# venv/lib/python3.8/site-packages/django/conf/__init__.pyの'settings'インスタンス変数
from django.conf import settings
# venv/lib/python3.8/site-packages/django/conf/urls/static.pyの'static'メソッド
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # ←1行追加
]

# 投稿した画像を表⽰するための設定
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)