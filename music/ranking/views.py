from django.shortcuts import render
from index.models import *
from django.views.generic import ListView

# Create your views here.
def rankingView(request):
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    labels = Label.objects.all()
    t = request.GET.get('type', '')
    if t:
        dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
    else:
        dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
    return render(request, 'ranking.html', locals())