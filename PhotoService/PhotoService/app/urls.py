# 新規作成ファイル
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    # トップページのurl生成
    path('', views.index, name='index'),
    # ユーザページのurl生成
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    # 投稿ページのurl生成
    path('photos/new/', views.photos_new, name='photos_new'),
    # 投稿詳細ページのurl生成
    path('photos/<int:pk>/', views.photos_detail, name='photos_detail'),
    # 削除ページのurl生成
    path(
        'photos/<int:pk>/delete/',
        views.photos_delete,
        name='photos_delete'
    ),
    # カテゴリー別ページのurl生成
    path(
        'photos/<str:category>/',
        views.photos_category,
        name='photos_category'
    ),
    # サインインページのurl生成
    path('signup/', views.signup, name='signup'),
    # ログインページのurl生成
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='app/login.html'),
        name='login'
    ),
    # ログアウトページのurl生成
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]