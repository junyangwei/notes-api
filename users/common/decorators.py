"""用户相关装饰器"""
from django.http import JsonResponse
from users.controller.users import set_cookie as setCookie

def login_required(function):
    """登陆限制"""

    def login_check(request, *args, **kwargs):
        """校验登陆状态session，并且清除session和cookie"""
        if not request.session.get('is_login', default=False):
            request.session.flush()
            return fail(msg='抱歉，需要登录后才能访问，请先登录!',
                        delCookie=True)

        return function(request, *args, **kwargs)

    return login_check

def fail(msg='', code=-1, delCookie=False):
    """失败返回函数"""
    result = {
        'code': code,
        'msg': msg,
        'data': None,
    }
    response = JsonResponse(result);

    # 是否需要清除Cookie，是则在返回时清除登陆Cookie信息
    if delCookie:
        setCookie(response, 'username', '', 0);
        setCookie(response, 'nickname', '', 0);

    return response
