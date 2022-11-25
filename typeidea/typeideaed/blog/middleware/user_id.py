# @Time      : 2022/11/25  上午11:12
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : user_id.py
# @Software  : PyCharm

import uuid

USER_KEY = 'uid'
TEN_YEARS = 60 * 60 * 24 * 365 * 10

class UserIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid


