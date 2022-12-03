from django.shortcuts import render
from django.views.generic import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import F

from .models import CommodityInfos, Types


# Create your views here.
def commodityView(request):
    title = '商品列表'
    calssContent = 'commoditys'

    firsts = Types.objects.values('firsts').distinct()
    typelists = Types.objects.all()

    t = request.GET.get('t', '')
    s = request.GET.get('s', 'sold')
    p = request.GET.get('p', '')
    n = request.GET.get('n', '')

    commodityInfos = CommodityInfos.objects.all()

    if t:
        types = Types.objects.filter(id=t).first()
        commodityInfos = commodityInfos.filter(types=types.seconds)

    if s:
        commodityInfos = commodityInfos.order_by('-'+s)

    if n:
        commodityInfos = commodityInfos.filter(name__contains=n)

    paginator = Paginator(commodityInfos, 6)

    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'commodity.html', locals())


def detailView(request, id):
    title = '商品介绍'
    classContent = 'details'

    commoditys = CommodityInfos.objects.filter(id=id).first()
    items = CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]
    likeList = request.session.get('likes', [])
    likes = True if id in likeList else False
    return render(request, 'details.html', locals())


def collectView(request):
    id = request.GET.get('id', '')
    result = {'result': '收藏'}
    likes = request.session.get('likes', [])
    if id and int(id) in likes:
        CommodityInfos.objects.filter(id=id).update(likes=F('likes')+1)
        result['result'] = '收藏成功'
        request.session['likes'] = likes + [int(id)]

    return JsonResponse(result)




class CommodityView(ListView):
    template_name = 'commodity.html'
    extra_context = {'title': '商品列表', 'classContent': 'commoditys'}
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firsts'] = Types.objects.values('firsts').distinct()
        context['typesList'] = Types.objects.all()

        return context


