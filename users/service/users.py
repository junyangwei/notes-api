import users.dao.users as users_dao
from hashlib import md5

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