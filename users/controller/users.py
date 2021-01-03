from django.http import JsonResponse, HttpResponse
from users.models import User
import json

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

    request.session.flush()
    return success(1)

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
    value = bytes(value, 'utf-8').decode('ISO-8859-1')
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
