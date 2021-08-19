# 新規作成ファイル
# venv/lib/python3.8/site-packages/django/contrib/auth/__init__.pyの'get_user_model'メソッド
from django.contrib.auth import get_user_model
# venv/lib/python3.8/site-packages/django/contrib/auth/forms.pyの'UserCreationForm'クラス
from django.contrib.auth.forms import UserCreationForm
# venv/lib/python3.8/site-packages/django/forms
from django import forms

# 新規会員登録機能
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)


# 「カートに追加」機能
class AddToCartForm(forms.Form):
    num = forms.IntegerField(
        label='数量',
        min_value=1,
        required=True
    )


# 郵便番号と住所を⼊⼒できるフォーム
class PurchaseForm(forms.Form):
    zip_code = forms.CharField(
        label='郵便番号',
        max_length=7,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': '数字7桁(ハイフンなし)'}
        )
    )
    address = forms.CharField(
        label='住所', max_length=100, required=False
    )