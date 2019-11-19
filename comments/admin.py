from django.contrib import admin

# Register your models here.

# 注册模型到管理后台

from .models import Comment

class CommnetAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']

admin.site.register(Comment, CommnetAdmin)
