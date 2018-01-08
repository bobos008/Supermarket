from django.shortcuts import render, HttpResponse, redirect
from hashlib import sha1
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
        is_seller = request.POST.get('is_seller')

        # 对秘密进行加密
        s1 = sha1()
        if is_seller == '0':
            username = request.POST.get('b_username')
            pwd = request.POST.get('b_pwd').encode("utf-8")
            s1.update(pwd)
            s1_pwd = s1.hexdigest()
        else:
            username = request.POST.get('s_username')
            pwd = request.POST('s_pwd').encode("utf-8")
            s1.update(pwd)
            s1_pwd = s1.hexdigest()
        print(s1_pwd)
        print(username)
        print(pwd)
        print(is_seller)
        return redirect('/login/')

# 用户登陆
def login(request):
    return render(request, 'sm_login/login.html')
