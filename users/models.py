from django.db import models

# 在这里创建需要的模型

class User(models.Model):
    """用户模型"""
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
