from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .form import *
from .models import *

# Create your views here.

@login_required(login_url='/shopper/login.html')
def shopperView(request):
    title = '个人中心'
    classContent = 'infomations'

    p = request.GET.get('p', 1)
    t = request.GET.get('t', '')
    payTime = request.session.get('payTime', '')
    if t and payTime and t==payTime:
        payInfo = request.session.get('payInfo', '')
        OrderInfos.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']

    orderinfos = OrderInfos.objects.filter(user_id=request.user.id).order_by('-created')

    paginator = Paginator(orderinfos,7)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'shopper.html', locals())

def loginView(request):
    title = '用户登陆'
    classContent = 'logins'

    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)  # 得到用户输入的表单数据
        data = infos.data
        username = data['username']
        password = data['password']

        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('shopper:shopper'))
            else:
                state = '注册成功'
        d = dict(username=username, password=password, is_staff=1, is_active=1)
        user = User.objects.create_user(**d)
        user.save()
    else:
        infos = LoginModelForm()
    return render(request, 'login.html', locals())


def logoutView(request):
    logout(request)
    return redirect(reverse('index:index'))

from commodity.models import *

@login_required(login_url='/shopper/login.html')
def shopCartView(request):
    title = '购物车'
    classContent = 'shopcarts'

    id = request.GET.get('id', '')
    quantity = request.GET.get('quantity', 1)
    userID = request.user.id

    if id:
        CartInfos.objects.update_or_create(commodityInfos=id, user_id=userID, quantity=quantity)
        return redirect('shopper:shopcart')

    getUserId = CartInfos.objects.filter(user_id=userID)
    commodityDict = {x.commodityInfos: x.quantity for x in getUserId}
    commodityInfos = CommodityInfos.objects.filter(id__in=commodityDict.keys())
    return render(request, 'shopcart.html', locals())

from django.http import JsonResponse

def deleteAPI(request):
    result = {'state': 'success'}
    userId = request.GET.get('userId', '')
    commodityId = request.GET.get('commodityId', '')
    if userId:
        CartInfos.objects.filter(user_id=userId).delete()
    elif commodityId:
        CartInfos.objects.filter(commodityInfos=commodityId).delete()
    else:
        result = {'state': 'fail'}
    return JsonResponse(result)

