#blog/model.py
import re
from django.forms import ValidationError

from django.db import models

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value):  #위도 경도 타입을 검사하는 
        raise ValidationError('invalid lnglat_type')                  #Validator

class Post(models.Model):
    STATUS_CHOICES =(
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )
    author = models.CharField(max_length=20) #blank 옵션을 주지 않았으므로 필수 필드
    title = models.CharField(max_length=100, verbose_name ='제목', help_text='포스팅 제목을 설정해 주세요, 최대 100자 내로 써주세요') #길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')             #길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank= True)
    lnglat = models.CharField(max_length=50, blank=True, 
            validators=[lnglat_validator],
            help_text='경도/위도 포맷으로 입력해 주세여')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True) # 생성 될 떄, 자동 저장
    updated_at = models.DateTimeField(auto_now=True)       # 갱신 될 때, 자동 갱신
    # 기본 정렬 설정
    class Meta:
        ordering = ['-id']

    # 글 title 보이기
    def __str__(self):
        return self.title
