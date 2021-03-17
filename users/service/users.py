import users.dao.users as users_dao
from hashlib import md5
from note_api.common.errors.biz_error import BizError
from note_api.common.errors.biz_status import biz_status as BizStatus

def login(username, password):
    """登陆校验接口，成功时返回用户信息"""
    if not (username and password):
        raise BizError(msg='用户名 / 密码不能为空')

    username = username.strip()
    password = password.strip()
    user = get_user_by_username(username)
    if not user:
        raise BizError(BizStatus['USER_PASSWORD_ERROR'])

    password_hash = get_password_hash(password)
    if user.password != password_hash:
        raise BizError(BizStatus['USER_PASSWORD_ERROR'])

    return user

def get_user_by_username(username):
    """获取用户根据用户名"""
    user = users_dao.get_user_by_username(username)
    return user

def create_user(username, password, nickname='', phone=None):
    """创建用户"""
    if not (username and password):
        raise BizError(msg='用户名 / 密码不能为空')

    username = username.strip()
    password = password.strip()

    if len(username) < 6 or len(username) > 18:
        raise BizError(msg='用户名长度必须在6~18位之间，请重新填写')

    if len(password) < 6 or len(password) > 18:
        raise BizError(msg='密码长度必须在6~18位之间，请重新填写')

    if phone and len(phone) != 11:
        raise BizError(msg='手机号长度必须为11位有效数字，请重新填写')

    exist_user = users_dao.get_user_by_username(username)
    if exist_user:
        raise BizError(msg='用户名已存在，请修改后再尝试')

    password_hash = get_password_hash(password)
    user = users_dao.create_user(username, password_hash, nickname, phone)
    if not user:
        raise BizError(msg='创建用户失败，请联系管理员')

    return user

def get_password_hash(password):
    """获取密码加密后的值"""
    secret = 'JAQi0MeaV1foLvR0'
    password_secret = str(password) + secret
    password_hash = md5(password_secret.encode(encoding='UTF-8')).hexdigest()
    return password_hash
