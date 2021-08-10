from django.shortcuts import render

# Create your views here.  以下追記
def index(request):
    return render(request, 'app/index.html')