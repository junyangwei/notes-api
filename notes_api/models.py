from django.db import models

# 在这里创建需要的模型

class Notes(models.Model):
    """笔记模型"""
    title = models.CharField(max_length=128, default='', verbose_name='笔记标题')
    content = models.TextField(blank=True, null=True, verbose_name='笔记内容')
    create_user_id = models.IntegerField(default=0, verbose_name='作者ID')
    status = models.IntegerField(default=1, verbose_name='状态 0无效 1有效')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        managed = False
        db_table = 'notes'

    def to_dict(note):
        note_dict = {
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'create_user_id': note.create_user_id,
            'status': note.status,
            'create_time': note.create_time,
            'update_time': note.update_time,
        }
        return note_dict

    def to_dicts(notes):
        notes_dict = []
        for note in notes:
            notes_dict.append(Notes.to_dict(note))
        return notes_dict

class NotesComment(models.Model):
    """笔记评论模型"""
    notes_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notes_comment'


class User(models.Model):
    """用户模型"""
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
