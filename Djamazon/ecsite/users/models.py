# venv/lib/python3.8/site-packages/django/db/modelsディレクトリ
from django.db import models
# venv/lib/python3.8/site-packages/django/contrib/auth/models.pyの'PermissionsMixin'クラス
from django.contrib.auth.models import PermissionsMixin
# venv/lib/python3.8/site-packages/django/contrib/auth/base_user.pyの'AbstractBaseUser'クラス
from django.contrib.auth.base_user import AbstractBaseUser
# venv/lib/python3.8/site-packages/django/utils/timezone.pyファイル
from django.utils import timezone
# venv/lib/python3.8/site-packages/django/contrib/auth/base_user.pyの'BaseUserManager'クラス
from django.contrib.auth.base_user import BaseUserManager
# app/models.pyの'Product'クラス
from app.models import Product

# Create your models here.
# カスタムユーザーマネージャークラスの作成
class UserManager(BaseUserManager):
    """カスタムユーザーマネージャー"""
    use_in_migrations = True

    # ユーザー情報を作成
    def _create_user(self, email, password, **extra_fields):
        # emailを必須にする
        if not email:
            # emailがない場合、値エラーを返す
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # emailを使ってUserデータを作成
        user = self.model(email=email, **extra_fields)
        # パスワードを設定
        user.set_password(password)
        # ユーザー情報をデータベースに保存
        user.save(using=self.db)
        return user

    # ユーザー情報を返す
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # superuserの情報を返す
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


# カスタムユーザーモデルの作成
class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    # 初期ポイント数
    initial_point = 50000
    # メールアドレス
    email = models.EmailField("メールアドレス", unique=True)
    # 保有ポイント
    point = models.PositiveIntegerField(default=initial_point)
    # お気に入り商品
    fav_products = models.ManyToManyField(Product, blank=True)
    # 
    is_staff = models.BooleanField("is_staff", default=False)
    # 
    is_active = models.BooleanField("is_active", default=True)
    # 登録日時
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"