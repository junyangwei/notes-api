"""定义notes_api的URL模式"""

from django.urls import path
from . import views
from .controller import home

app_name='notes_api';
urlpatterns = [
    # 主页
    path('', home.index, name='index'),
    # 获取csrf_token
    path('get_csrf', home.get_csrf),
    # 获取所有笔记
    path('notes', home.get_notes),
    # 获取特定笔记详情
    path('notes/<int:note_id>', home.get_note_detail),
    # 创建笔记
    path('create_note', home.create_note),
    # 更新笔记
    path('update_note', home.update_note),
]
