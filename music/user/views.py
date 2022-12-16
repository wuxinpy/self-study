from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .models import *
from .form import MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from index.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

def loginView(request):
    user = MyUserCreationForm()
    if request.method == 'POST':
        if request.POST.get('loginUser', ''):
            u = request.POST.get('loginUser', '')
            p = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=u) | Q(username=u)):
                u1 = MyUser.objects.filter(Q(mobile=u) | Q(username=u)).first()
                if check_password(p, u1.password):
                    login(request, u1)
                    return redirect(reverse('index'))
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        else:
            u = MyUserCreationForm(request.POST)
            if u.is_valid():
                u.save()
                tips = '注册成功'
            else:
                if u.errors.get('username', ''):
                    tips = u.errors.get('username', '注册失败')
                else:
                    tips = u.errors.get('mobile', '注册失败')
    return render(request, 'user.html', locals())


@login_required(login_url='/user/login.html')
def homeView(request, page):
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    songs = request.session.get('play_list', [])
    paginator = Paginator(songs, 3)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())

def logoutView(request):
    logout(request)
    return redirect('/')

