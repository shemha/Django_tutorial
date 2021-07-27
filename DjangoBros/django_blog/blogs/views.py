from django.shortcuts import render
from .models import Blog  # 追加

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})