from django.forms import ModelForm
from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        # Photo モデル
        model = Photo
        # 各フォーム
        fields = ['title', 'comment', 'image', 'category']