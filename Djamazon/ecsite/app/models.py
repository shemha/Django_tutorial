# venv/lib/python3.8/site-packages/django/db/modelsディレクトリ
from django.db import models
# venv/lib/python3.8/site-packages/django/auth/__init__.pyの'get_user_model'メソッド
from django.contrib.auth import get_user_model

# Create your models here.
# 商品モデル
class Product(models.Model):
    """商品"""
    # 商品名
    name = models.CharField(max_length=100)
    # 商品情報
    description = models.TextField(blank=True)
    # 商品価格
    price = models.PositiveIntegerField(default=0)
    # 商品イメージ
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name

# 売上情報モデル
class Sale(models.Model):
    """売上情報"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField("購⼊個数", default=0)
    price = models.PositiveIntegerField("商品単価")
    total_price = models.PositiveIntegerField("⼩計")
    created_at = models.DateTimeField(auto_now=True)