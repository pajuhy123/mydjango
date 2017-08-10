#blog/model.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name ='제목', help_text='포스팅 제목을 설정해 주세요') #길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')             #길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add = True) # 생성 될 떄, 자동 저장
    updated_at = models.DateTimeField(auto_now=True)       # 갱신 될 때, 자동 갱신
