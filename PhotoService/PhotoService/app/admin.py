from django.contrib import admin
from .models import Photo  # 追加

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Photo, PhotoAdmin)