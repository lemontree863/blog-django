from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):  # 表单类必需继承自forms.Form或forms.ModeForm
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
