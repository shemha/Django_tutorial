from django.shortcuts import render, get_object_or_404  # 'get_object_or_404'を追加
from .models import Blog  # 追加
from .forms import BlogForm  # 追加

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})

def detail(request, blog_id):
#   blog = Blog.objects.get(id=blog_id) 直下に修正
    blog = get_object_or_404(Blog, id=blog_id)  # 上をこちらに修正
    return render(request, 'blogs/detail.html', {'blog': blog})

def new(request):
    form = BlogForm
    return render(request, 'blogs/new.html', {'form': form})