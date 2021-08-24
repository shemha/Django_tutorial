# venv/lib/python3.8/site-packages/django/forms/models.pyのModelFormクラス
from django.forms import ModelForm
# アプリケーションディレクトリにあるmodels.pyのBlogクラス
from .models import Blog

# ModelFormクラスを継承
# 新規ブログ投稿フォームを生成
class BlogForm(ModelForm):
    class Meta:
        # Blogクラスをクラス変数'model'に代入
        model = Blog
        # タイトルと投稿内容のフィールドを生成
        fields = ['title', 'text']