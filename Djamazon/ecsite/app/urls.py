# 新規作成ファイル
# venv/lib/python3.8/site-packages/django/url/conf.pyの'path'変数
from django.urls import path
# app/views.pyを利用
from . import views
# venv/lib/python3.8/site-packages/django/contrib/auth/views.pyファイル
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    # トップページ
    path('', views.index, name='index'),
    # サインアップページ
    path('signup/', views.signup, name='signup'),
    # ログインページ
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='app/login.html'),
        name='login'
    ),
    # ログアウトページ
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 商品ページ
    path('product/<int:product_id>/', views.detail, name='detail'),
    # お気に⼊りページ
    path('fav_products/', views.fav_products, name='fav_products'),
    path(
        'toggle_fav_product_status/',
        views.toggle_fav_product_status,
        name='toggle_fav_product_status'
    ),
    # カートページ
    path('cart/', views.cart, name='cart'),
    path(
        'change_product_amount/',
        views.change_product_amount,
        name='change_product_amount'
    ),
    # 注⽂履歴ページ
    path('order_history/', views.order_history, name='order_history'),
]