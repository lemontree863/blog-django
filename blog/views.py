from django.shortcuts import render

# Create your views here.
# servlet

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Post, Category, Tag
import markdown
import re


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request=request, template_name='blog/index.html', context={
        # 'title': '我的博客首页',
        # 'welcome': '欢迎访问我的博客首页'
        'post_list': post_list
    })


# def detail(request, pk):
#     post = get_object_or_404(Post, id=pk)  # 第一个参数：类 第二个参数类属性id=？必需指定id,否则报错
#     post.body = markdown.markdown(post.body, extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       'markdown.extensions.toc',
#                                   ])  # ![图片说明](图片链接)
#     return render(request, 'blog/detail.html', context={
#         'post': post
#     })

def detail(request, pk):
    post = get_object_or_404(Post, id=pk)  # 第一个参数：类 第二个参数类属性id=？必需指定id,否则报错
    # 阅读量+1
    post.increase_views()
    md = markdown.Markdown(extensions=[  # 实例化markdown , 大写的Markdown
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)  # 优化锚点展示
    ])  # ![图片说明](图片链接)
    post.body = md.convert(post.body)
    # post.toc = md.toc

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={
        'post': post
    })


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})














