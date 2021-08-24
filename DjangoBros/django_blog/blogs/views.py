# venv/lib/python3.8/site-packages/django/shortcuts.pyのrender関数,redirect関数,get_object_or_404関数
from django.shortcuts import render, redirect, get_object_or_404
# アプリケーションディレクトリにあるmodels.pyのBlogクラス
from .models import Blog
# アプリケーションディレクトリにあるforms.pyのBlogFormクラス
from .forms import BlogForm
# # venv/lib/python3.8/site-packages/django/views/decorators/http.pyのrequire_POST変数
from django.views.decorators.http import require_POST

# Create your views here.
# トップページの表示設定
def index(request):  # ユーザーからのリクエスト情報が実引数
    # Blogクラスのオブジェクトを投稿日の降順に並べる
    blogs = Blog.objects.order_by('-created_datetime')
    # index.htmlを表示、HTML内のblogsにBlogクラスのオブジェクトを表示
    return render(request, 'blogs/index.html', {'blogs': blogs})

# 詳細ページの表示設定
def detail(request, blog_id):  # ユーザーからのリクエスト情報とブログのIDが実引数
    # # BlogクラスのオブジェクトをIDで照合
    # blog = Blog.objects.get(id=blog_id)
    # 指定のIDでページがない場合に対応できるよう下記に変更
    # BlogクラスのオブジェクトをIDで照合し、オブジェクトがあるか無いか判定
    blog = get_object_or_404(Blog, id=blog_id)
    # detail.htmlを表示、HTML内のblogにBlogクラスのオブジェクトを表示
    return render(request, 'blogs/detail.html', {'blog': blog})

# 新規投稿ページの表示設定
def new(request):  # ユーザーからのリクエスト情報が実引数
    # リクエスト情報がPOSTで送信されてきた場合
    if request.method == "POST":
        # 受け取ったPOST情報をBlogFormクラスのクラス変数に代入した状態をformに代入
        form = BlogForm(request.POST)
        # 受け取った情報にエラーがないか検証
        if form.is_valid():
            # POST情報をデータベースへ保存
            form.save()
            # トップページへ遷移
            return redirect('blogs:index')
    # POST情報以外の場合
    else:
        # BlogFormクラスをformに代入
        form = BlogForm
    # new.htmlを表示、HTML内のformにBlogFormクラスで定義した入力フォームを表示
    return render(request, 'blogs/new.html', {'form': form})

# 削除ページの表示設定
@require_POST  # リクエスト情報がPOSTの場合に実行する関数としてデコレート
def delete(request, blog_id):  # ユーザーからのリクエスト情報とブログのIDが実引数
    # BlogクラスのオブジェクトをIDで照合し、オブジェクトがあるか無いか判定
    blog = get_object_or_404(Blog, id=blog_id)
    # オブジェクト情報を削除
    blog.delete()
    # トップページへ遷移
    return redirect('blogs:index')

# 編集ページの表示設定
def edit(request, blog_id):  # ユーザーからのリクエスト情報とブログのIDが実引数
    # BlogクラスのオブジェクトをIDで照合し、オブジェクトがあるか無いか判定
    blog = get_object_or_404(Blog, id=blog_id)
    # リクエスト情報がPOSTで送信されてきた場合
    if request.method == "POST":
        # 受け取ったPOST情報をBlogFormクラスのクラス変数に代入した状態をformに代入
        form = BlogForm(request.POST, instance=blog)  # 'instance=blog'でもともと保存されてあった内容を表⽰させる
        # 受け取った情報にエラーがないか検証
        if form.is_valid():
            # POST情報をデータベースへ保存
            form.save()
            # 詳細ページへ遷移
            return redirect('blogs:detail', blog_id=blog_id)
    # POST情報以外の場合
    else:
        # BlogFormクラスをformに代入
        form = BlogForm(instance=blog)  # 'instance=blog'でもともと保存されてあった内容を表⽰させる
    # edit.htmlを表示、HTML内のformにBlogFormクラスで定義した入力フォームとblogにBlogクラスのオブジェクトを表示
    return render(request, 'blogs/edit.html', {'form': form, 'blog':blog})