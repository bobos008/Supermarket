from django.shortcuts import render, HttpResponse, redirect 
from django.http import JsonResponse
from hashlib import sha1
from .models import Seller, Buyer


# Create your views here.
def test1(request):
	return HttpResponse("首页")


# 用户注册
def register(request):
    # b_username = request.POST.get('b_username')
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
            buyer_info = {
                'b_name' : username,
                'b_password' : s1_pwd
            }
            try:
                Buyer.objects.create(**buyer_info)
            except Exception:
                return 
        else:
            username = request.POST.get('s_username')
            pwd = request.POST.get('s_pwd').encode('utf-8')
            s1.update(pwd)
            s1_pwd = s1.hexdigest()
            seller_info = {
                's_name' : username,
                's_password' : s1_pwd,
            }
            Seller.objects.create(**seller_info)

        return redirect('/login/')


# 验证用户名是否重复
def username_is_repeat(request):
    is_seller = request.GET.get('is_seller')
    if is_seller == '0':
        username = request.GET.get('username', '')
        res = Buyer.objects.filter(b_name = username).exists()
    else:
        username = request.GET.get('username', '')
        res = Seller.objects.filter(s_name = username).exists()
    return JsonResponse({'data': res}) 


# 用户登陆
def login(request):
    return render(request, 'sm_login/login.html')


# 判断用户密码是否正确
def is_login(request):
    is_buyer = request.GET.get('is_buyer', '0')
    user = request.GET.get('username', "")
    pwd = request.GET.get('pwd', "").encode('utf-8')
    s1 = sha1()

    if is_buyer == '0':
        u_res = Buyer.objects.filter(b_name = user).exists()
        if u_res:
            s1.update(pwd) 
            s1_pwd = s1.hexdigest()
            p_res = Buyer.objects.filter(b_name = user, b_password = s1_pwd).exists()
            if p_res:
                return redirect('/test1/')
            else:
                res = 1
        else:
            res = 0
    else:
        u_res = Seller.objects.filter(s_name = user).exists()
        if u_res:
            s1.update(pwd)
            s1_pwd = s1.hexdigest()
            p_res = Seller.objects.filter(s_name = user, s_password = s1_pwd).exists()
            if p_res:
                return redirect('/test1/')
            else:
                res = 1
        else:
            res = 0
    return JsonResponse({'data' : res})
