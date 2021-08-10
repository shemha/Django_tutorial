from django.shortcuts import render, get_object_or_404  # 'get_object_or_404'を追加

# Create your views here.  下記追加
def index(request):
    return render(request, 'app/index.html')

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'app/users_detail.html', {'user': user})