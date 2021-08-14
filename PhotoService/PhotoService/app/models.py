from django.db import models
from django.contrib.auth.models import User  # ←ユーザ情報追加

# Create your models here.
# Category モデルを作成
class Category(models.Model):
    # 投稿タイトル
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# Photo モデルを作成
class Photo(models.Model):
    # 投稿タイトル
    title = models.CharField(max_length=150)
    # 投稿内容
    comment = models.TextField(blank=True)
    # 投稿写真
    image = models.ImageField(upload_to='photos')
    # 投稿カテゴリー
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # 投稿者
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 投稿日時
    created_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title