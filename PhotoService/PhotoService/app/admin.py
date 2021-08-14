from django.contrib import admin  # ←管理者情報を読み込み
from .models import Category, Photo  # ←'Category'モデル, 'Photo'モデルを読み込み

# Register your models here.
# 管理者ページの'Category'内容
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 管理者ページの'Photo'内容
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 管理者ページの'Category'設定
admin.site.register(Category, CategoryAdmin)
# 管理者ページの'Photo'設定
admin.site.register(Photo, PhotoAdmin)