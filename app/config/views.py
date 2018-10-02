from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    # 곧바로 /polls로 redirect 되도록 설정
    return redirect('index')