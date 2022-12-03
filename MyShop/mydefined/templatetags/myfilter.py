# @Time      : 2022/12/3  下午3:52
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : myfilter.py
# @Software  : PyCharm

from django import template

register = template.Library()

@register.filter(name='replace')
def do_replace(values, args):
    oldValue = args.split(':')[0]
    newValue = args.split(':')[1]
    return values.replace(oldValue, newValue)

