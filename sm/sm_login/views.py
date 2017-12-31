from django.shortcuts import render, HttpResponse

# Create your views here.
def test1(request, id1):
	return HttpResponse('test1=%s'%id1)

# 用户注册
def register(request):
    return render(request, 'sm_login/register')

# 用户登陆
def login(request):
    return render(request, 'sm_login/login.html')
