from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def test1(request, id1):
	return HttpResponse('test1=%s'%id1)

# 用户注册
def register(request):
    # b_username = request.POST.get('b_username')
    print("=====================register")
    print(request.method)
    now_method = request.method
    if now_method == 'GET':
        return render(request, 'sm_login/register.html')
    else:
        username = request.POST.get('b_username')
        pwd = request.POST.get('b_pwd')
        is_seller = request.POST.get('is_seller')
        print(username)
        print(pwd)
        print(is_seller)
        return redirect('/login/')

# 用户登陆
def login(request):
    return render(request, 'sm_login/login.html')
