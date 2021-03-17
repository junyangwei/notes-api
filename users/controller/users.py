from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import json
from urllib import parse
from users.models import User
from users.service import users as users_service


@require_http_methods(['POST'])
def login(request):
    """用户登录"""
    json_data = json.loads(request.body) 
    username = json_data.get('username')
    password = json_data.get('password')

    user = users_service.login(username, password)

    # 设置session
    set_session_user(request, user)

    # 设置cookie并返回
    result = format_success_data(get_session_user(request))
    response = JsonResponse(result)
    max_age = request.session.get_session_cookie_age()
    set_cookie(response, 'username', user.username, max_age)
    set_cookie(response, 'nickname', user.nickname, max_age)
    return response

def logout(request):
    """退出登录"""
    if not request.session.get('is_login', default=False):
        return fail('抱歉，您还未登陆，不允许进行退出登录操作')

    result = format_success_data(1);
    response = JsonResponse(result);
    set_cookie(response, 'username', '', 0);
    set_cookie(response, 'nickname', '', 0);
    request.session.flush()
    return response

@require_http_methods(['POST'])
def register(request):
    """用户注册"""
    json_data = json.loads(request.body)
    username = json_data.get('username')
    password = json_data.get('password')
    nickname = json_data.get('nickname')
    phone = json_data.get('phone')

    user = users_service.create_user(username, password, nickname, phone)

    # 设置session
    set_session_user(request, user)

    # 设置cookie并返回
    result = format_success_data(get_session_user(request))
    response = JsonResponse(result)
    max_age = request.session.get_session_cookie_age()
    set_cookie(response, 'username', user.username, max_age)
    set_cookie(response, 'nickname', user.nickname, max_age)
    return response

def get_session_user(request):
    """获取session中的用户信息字典"""
    session_user = {
        'user_id': request.session.get('user_id', default=0),
        'username': request.session.get('username', default=None),
        'nickname': request.session.get('nickname', default=None),
        'phone': request.session.get('phone', default=None),
    }
    return session_user

def set_session_user(request, user):
    """设置用户信息的session"""
    request.session['is_login'] = True
    request.session['user_id'] = user.id
    request.session['username'] = user.username
    request.session['nickname'] = user.nickname
    request.session['phone'] = user.phone

def format_success_data(argData='', msg=''):
    """拼接返回函数"""
    result = {
        'code': 0,
        'msg': msg,
        'data': argData,
    }
    return result

def set_cookie(response, key='', value='', max_age=1209600):
    key = parse.quote(key)
    value = parse.quote(value) if value else ''
    response.set_cookie(key, value, max_age)

def success(argData='', msg=''):
    """成功返回函数"""
    result = {
        'code': 0,
        'msg': msg,
        'data': argData,
    }
    return JsonResponse(result)

def fail(msg='', code=-1):
    """失败返回函数"""
    result = {
        'code': code,
        'msg': msg,
        'data': None,
    }
    return JsonResponse(result)
