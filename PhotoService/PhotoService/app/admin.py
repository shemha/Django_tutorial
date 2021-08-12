from django.contrib import admin
from .models import Category, Photo  # ←1行追加(さらに'Category'を追加)

# Register your models here.  下記追加
# カテゴリのクラス
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 写真のクラス
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)