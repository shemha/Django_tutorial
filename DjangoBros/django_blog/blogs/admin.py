# venv/lib/python3.8/site-packages/django/contrib/adminディレクトリ
from django.contrib import admin
# アプリケーションディレクトリ/models.pyのBlogクラス
from .models import Blog

# Register your models here.
# adminディレクトリにあるoptions.pyのBaseModelAdminクラスを継承したModelAdminクラスを継承
class BlogAdmin(admin.ModelAdmin):
    # 表示する項目
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    # リンクを付与した項目
    list_display_links = ('id', 'title')


# 管理サイトにBlogクラスの情報を表示
# adminディレクトリにあるsites.pyのsite変数の持つregisterメソッドを実行
admin.site.register(Blog, BlogAdmin)