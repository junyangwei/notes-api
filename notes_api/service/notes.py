import notes_api.dao.notes as notes_dao

def get_notes():
    """获取笔记"""
    notes = notes_dao.get_notes()
    return notes

def get_note_detail(note_id):
    """获取特定笔记详情"""
    note = notes_dao.get_note_detail(note_id)
    return note

def create_note(title, content='', create_user_id=0, status=1):
    """写入新的笔记"""
    newNoteId = notes_dao.create_note(title, content, create_user_id, status)
    return newNoteId

def update_note(note_id, title, content):
    """更新笔记"""
    noteId = notes_dao.update_note(note_id, title, content)
    return noteId
