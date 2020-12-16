from django.contrib import admin

# 在这里注册模型
from notes_api.models import Notes

admin.site.register(Notes)
