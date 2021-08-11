from django.shortcuts import render, get_object_or_404, redirect  # 'get_object_or_404', 'redirect'を追加
from django.contrib.auth.models import User  # 追加
from .models import Photo  # 追加

# Create your views here.  下記追加
def index(request):
    # Photoインスタンスを全件取得
    photos = Photo.objects.all().order_by('-created_at')
    # 取得したPhotoインスタンスをテンプレートに渡す
    return render(request, 'app/index.html', {'photos': photos})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'app/users_detail.html', {'user': user})