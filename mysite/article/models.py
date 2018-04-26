from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #作者

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)     #(default=timezone.now)
    last_update_time=models.DateTimeField(auto_now=True)    
    auther=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)        #DO_NOTHING表示删除该article后不会对作者字段产生任何影响；1表示当前用户
    is_deleted = models.BooleanField(default=False)
    reader_num = models.IntegerField(default=0)
    
    def __str__(self):      #对类显示的内容进行初始化
        return "<Article: %s>" %self.title
        