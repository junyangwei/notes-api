"""笔记数据库操作"""
from .db import DBConnect
import MySQLdb
from notes_api.models import Notes
from django.core import serializers

def get_notes():
    notes = Notes.objects.all()
    return Notes.to_dicts(notes)

def get_note_detail(note_id):
    note = Notes.objects.get(id=note_id)
    return Notes.to_dict(note)

def create_note(title='无标题', content='', create_user_id=0, status=1):
    note = Notes(title=title, content=content, create_user_id=create_user_id,
                 status=status)
    note.save()
    return note.id

def update_note(note_id, title, content):
    # 防止传入数据格式有误，做一层数据转换
    int_note_id = int(note_id)
    note = Notes.objects.get(id=int_note_id)
    if title:
        note.title = str(title)
    if content:
        note.content = str(content)
    note.save()
    return int_note_id

def get_all_notes():
    sql = "SELECT id, title, content FROM notes WHERE STATUS = 1;"
    db = DBConnect()
    db.cur.execute(sql)
    return db.cur.fetchall()
