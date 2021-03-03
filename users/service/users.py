import users.dao.users as users_dao
from hashlib import md5
from note_api.common.errors.biz_error import BizError
from note_api.common.errors.biz_status import biz_status as BizStatus

def login(username, password):
    """登陆校验接口，成功时返回用户信息"""
    if not (username and password):
        raise BizError(msg='缺少入参：账号 / 密码')

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

def create_user(username, password, nickname='', phone=None, status=1):
    """创建用户"""
    user = users_dao.create_user(username, password, nickname, phone, status)
    return user

def get_password_hash(password):
    """获取密码加密后的值"""
    secret = 'JAQi0MeaV1foLvR0'
    password_secret = str(password) + secret
    password_hash = md5(password_secret.encode(encoding='UTF-8')).hexdigest()
    return password_hash
