from django.shortcuts import render, get_object_or_404, redirect  # 'get_object_or_404', 'redirect'を追加
from django.contrib.auth.models import User  # ←ユーザ情報追加
from .models import Photo  # ←画像表示追加
from django.contrib.auth.forms import UserCreationForm  # ←ユーザ登録追加
from django.contrib.auth import authenticate, login  # ←ログインフォーム追加
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Photo, Category

# Create your views here.
# トップページの表示
def index(request):
    # Photoインスタンスを全件取得
    photos = Photo.objects.all().order_by('-created_at')
    # 取得したPhotoインスタンスをテンプレートに渡す
    return render(request, 'app/index.html', {'photos': photos})

# ユーザページの表示
def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    # userに紐づく写真⼀覧を取得
    photos = user.photo_set.all().order_by('-created_at')
    # photosを追加
    return render(request, 'app/users_detail.html', {'user': user, 'photos': photos})

# サインアップを表示
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Userインスタンスを作成
        if form.is_valid():
            form.save() # Userインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの⼊⼒値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(
                username=input_username,
                password=input_password,
            )
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # login関数は、認証ができてなくてもログインさせることができる。(認証は上のauthenticateで実⾏する)
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

# 写真投稿ページを表示
@login_required  # デコレータ(関数の機能的に装飾)：ログインしてなければ関数を実⾏せずログイン画⾯(settings.pyで設定したLOGIN_URL)にリダイレクト、ログインしているユーザーだけ関数を実行
def photos_new(request):
    if request.method == "POST":  # POSTされた情報を元にフォーム情報を⽣成
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)  # ⼊⼒された情報からPhotoインスタンスを⽣成
            photo.user = request.user  # ⽣成したPhotoインスタンスのuserフィールドに、request.user(写真を投稿したUserのオブジェクト)を代⼊
            photo.save()  # インスタンスをデータベースに保存
            messages.success(request, "投稿が完了しました!")  # 正常にアップロードされた場合に成功メッセージを表⽰
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'app/photos_new.html', {'form': form})

# 写真投稿詳細ページの表示
def photos_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/photos_detail.html', {'photo': photo})

# 投稿削除ページの表示
@require_POST
def photos_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk, user=request.user)
    photo.delete()
    return redirect('app:users_detail', request.user.id)

# カテゴリー別ページを表示
def photos_category(request, category):
    # titleがURLの⽂字列と⼀致するCategoryインスタンスを取得
    category = get_object_or_404(Category, title=category)
    # 取得したCategoryに属するPhoto⼀覧を取得
    photos = Photo.objects.filter(category=category).order_by('-created_at')
    return render(
        request, 'app/index.html', {'photos': photos, 'category': category}
    )