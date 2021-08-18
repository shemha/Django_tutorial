# venv/lib/python3.8/site-packages/django/contrib/adminディレクトリ
from django.contrib import admin
# app/models.pyの'Product'クラス, 'Sale'クラス
from .models import Product, Sale

# Register your models here.
# 商品情報ページ
admin.site.register(Product)
# 売上情報ページ
admin.site.register(Sale)