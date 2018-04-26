from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","auther","is_deleted","create_time","last_update_time")          #设置为一个元组，不可变
    ordering = ("-id",)              #后面写个逗号表示是一个元组
    
admin.site.register(Article, ArticleAdmin)        #将应用注册到管理系统