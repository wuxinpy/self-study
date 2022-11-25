# @Time      : 2022/11/20  下午3:08
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : adminforms.py
# @Software  : PyCharm

from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)