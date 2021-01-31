from django.http import JsonResponse, HttpResponse
import notes_api.dao.notes as notes_dao
from notes_api.service import notes as notes_service
from django.template.context_processors import csrf
import json
from users.common.decorators import login_required

from notes_api.forms import NoteForm

def index(request):
    """主页"""
    return success('Hello World!')

def get_csrf(request):
    """生成csrf数据，给前端"""
    csrf_data = csrf(request)
    csrf_token = csrf_data['csrf_token']
    return success(str(csrf_token))
    # return HttpResponse('{}'.format(csrf_token))
    # return HttpResponse(str(csrf_token))

@login_required
def get_notes(request):
    notes = notes_service.get_notes();
    return success(notes)

@login_required
def get_note_detail(request, note_id):
    note = notes_service.get_note_detail(note_id)
    return success(note)

@login_required
def create_note(request):
    """添加新笔记"""
    if request.method != 'POST':
        return success()

    # 使用Django的表单获取传入参数示例
    # form = NoteForm(request.POST)
    # if form.is_valid():
        # form.save()

    # 使用x-www-form-urlencoded方法传入，获取参数示例
    # request_body = request.POST
    # title = request.POST['title']
    # content = request.POST['content']

    # 使用JSON方法传入，获取参数示例
    json_data = json.loads(request.body) 
    title = json_data['title']
    content = json_data['content']
    newNoteId = notes_service.create_note(title, content)
    return success(newNoteId)

@login_required
def update_note(request):
    """更新笔记"""
    if request.method != 'POST':
        return success()

    # 使用JSON方法传入，获取参数示例
    json_data = json.loads(request.body)
    note_id = json_data['note_id']
    title = json_data['title']
    content = json_data['content']
    noteId = notes_service.update_note(note_id, title, content)
    return success(noteId)

@login_required
def get_all_notes(request):
    """获取所有笔记"""
    all_notes = notes_dao.get_all_notes()
    return success(all_notes)

def success(argData='', msg=''):
    """成功返回函数"""
    result = {
        'code': 0,
        'msg': msg,
        'data': argData,
    }
    return JsonResponse(result)
