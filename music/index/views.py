from django.shortcuts import render
from .models import *

# Create your views here.
def indexView(request):
    songDynamic = Dynamic.objects.select_related('song')
    searchs = songDynamic.order_by('-search').all()[:8]
    labels = Label.objects.all()
    popular = songDynamic.order_by('-plays').all()[:10]
    recommend = Song.objects.order_by('-release').all()[:3]
    downloads = songDynamic.order_by('-download').all()[:6]
    tabs = [searchs[:6], downloads]
    return render(request, 'index.html', locals())

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def page_error(request):
    return render(request, '404.html', status=500)

