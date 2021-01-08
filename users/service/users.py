import users.dao.users as users_dao

def get_user_by_username(username):
    """获取用户根据用户名"""
    user = users_dao.get_user_by_username(username)
    return user

def create_user(username, password, nickname='', phone=None, status=1):
    """创建用户"""
    user = users_dao.create_user(username, password, nickname, phone, status)
    return user