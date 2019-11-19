from django import template
from ..models import Post, Category, Tag

register = template.Library()

# 自定义模板标签
#  blog 应用下创建一个 templatetags 文件夹。然后在这个文件夹下创建一个 __init__.py 文件，
#  使这个文件夹成为一个 Python 包，之后在 templatetags
#  目录下创建一个 blog_extras.py 文件，这个文件存放自定义的模板标签代码。
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }
