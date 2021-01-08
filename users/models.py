from django.db import models

# 在这里创建需要的模型

class User(models.Model):
    """用户模型"""
    username = models.CharField(max_length=64, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    nickname = models.CharField(max_length=64, blank=True, null=True, verbose_name='昵称')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='手机号')
    status = models.IntegerField(default=1, verbose_name='状态 0无效 1有效')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        managed = False
        db_table = 'user'

    def to_dict(user):
        user_dict = {
            'id': user.id,
            'username': user.username,
            'pssword': user.password,
            'nickname': user.nickname,
            'phone': user.phone,
            'status': user.status,
            'create_time': user.create_time,
            'update_time': user.update_time,
        }
        return user_dict