from django.shortcuts import render
#coding=utf-8
from django.shortcuts import render
from homepage.models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'blog_list': blog_list})
# Create your views here.


