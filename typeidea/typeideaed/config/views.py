from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from blog.views import CommentViewMixin
from .models import Link


class LinkListView(CommentViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'