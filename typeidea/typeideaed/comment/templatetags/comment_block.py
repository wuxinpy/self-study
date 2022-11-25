# @Time      : 2022/11/24  下午9:40
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : comment_block.py
# @Software  : PyCharm

from django import template

from ..forms import CommentForm
from ..models import Comment

register = template.Library()


@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }
