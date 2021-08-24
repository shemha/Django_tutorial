from django.db import models

# Create your models here.
# データベースのフィールドを作成
class Blog(models.Model):
    # 空欄不可、最大文字数150の「タイトル用」テキストフィールド
    title = models.CharField(blank=False, null=False, max_length=150)
    # 空欄不可の「投稿用」テキストフィールド
    text = models.TextField(blank=True)
    # 「投稿日」のフィールド
    created_datetime = models.DateTimeField(auto_now_add=True)
    # 「更新日」のフィールド
    updated_datetime = models.DateTimeField(auto_now=True)

    # 文字列を操作する組み込み関数(print(),format(),etc.)が実行された時に実行する特殊メソッド
    def __str__(self):
        return self.title  # ブログ記事のタイトルを表示