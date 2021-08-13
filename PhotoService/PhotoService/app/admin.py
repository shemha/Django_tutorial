from django.contrib import admin
from .models import Category, Photo  # ←1行追加

# Register your models here.
# 管理者ページの'Category'設定
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 管理者ページの'Photo'設定
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)