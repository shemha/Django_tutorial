from django.shortcuts import render, redirect, get_object_or_404  # 'get_object_or_404'、'redirect'を追加
from .models import Blog  # 追加
from .forms import BlogForm  # 追加
from django.views.decorators.http import require_POST # 追加

# Create your views here.
def index(request):  # ブログ管理ページ
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})

def detail(request, blog_id):  # 詳細ページ
#   blog = Blog.objects.get(id=blog_id) 直下に修正
    blog = get_object_or_404(Blog, id=blog_id)  # 上をこちらに修正
    return render(request, 'blogs/detail.html', {'blog': blog})

def new(request):  # 新規ブログ記事投稿ページ
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogForm
    return render(request, 'blogs/new.html', {'form': form})

@require_POST
def delete(request, blog_id):  # Delete機能
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blogs:index')