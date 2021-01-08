"""用户数据库操作"""
from users.models import User

def get_user_by_username(username):
    """获取用户信息根据用户名"""
    try:
        user = User.objects.get(username=username)
    except:
        return None
    return user

def create_user(username, password, nickname='', phone=None, status=1):
    """创建新的用户"""
    user = User(username=username, password=password, nickname=nickname,
                phone=phone, status=status)
    user.save()
    return user