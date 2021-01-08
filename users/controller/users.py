from django.http import JsonResponse, HttpResponse
from users.models import User
import json
from urllib import parse
from users.service import users as users_service

def login(request):
    """用户登录"""
    if request.method != 'POST':
        return fail('调用方法不正确，请检查调用方式')

    # if request.session.get('is_login', default=False):
    #     return success(get_session_user(request))

    json_data = json.loads(request.body) 
    username = json_data['username']
    password = json_data['password']
    if username and password:
        username = username.strip()
        try:
            user = User.objects.get(username=username)
        except:
            return fail('用户信息不存在，请确认后再尝试')

        if user.password != password:
            return fail('账号或密码错误，请确认后再尝试')

        # 设置session
        set_session_user(request, user)

        # return success(get_session_user(request))

        # 设置cookie并返回
        result = format_success_data(get_session_user(request))
        response = JsonResponse(result)
        max_age = request.session.get_session_cookie_age()
        set_cookie(response, 'username', user.username, max_age)
        set_cookie(response, 'nickname', user.nickname, max_age)
        return response

    return fail('缺少入参：账号 / 密码')

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

def register(request):
    """用户注册"""
    if request.method != 'POST':
        return fail('调用方法不正确，请检查调用方式')

    json_data = json.loads(request.body)
    username = json_data.get('username').strip()
    password = json_data.get('password').strip()
    nickname = json_data.get('nickname')
    phone = json_data.get('phone')
    if not username or not password:
        return fail('用户名/密码不能为空')

    if len(password) < 6:
        return fail('密码长度不得低于6位，请重新填写')

    user = users_service.get_user_by_username(username)
    if user:
        return fail('用户名已存在，请修改后再尝试')

    user = users_service.create_user(username, password, nickname, phone)
    if not user:
        return fail('创建用户失败，请联系管理员')

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
