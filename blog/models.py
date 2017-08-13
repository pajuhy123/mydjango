#blog/model.py
import re
from django.conf import settings
from django.forms import ValidationError
from django.core.urlresolvers import reverse

from django.db import models

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):  #위도 경도 타입을 검사하는 
        raise ValidationError('invalid lnglat_type')                  #Validator

class Post(models.Model):
    STATUS_CHOICES =(
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #author = models.CharField(max_length=20) #blank 옵션을 주지 않았으므로 필수 필드
    title = models.CharField(max_length=100, verbose_name ='제목', help_text='포스팅 제목을 설정해 주세요, 최대 100자 내로 써주세요') #길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')             #길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank= True)
    lnglat = models.CharField(max_length=50, blank=True, 
            validators=[lnglat_validator],
            help_text='경도/위도 포맷으로 입력해 주세여')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set =  models.ManyToManyField('Tag', blank= True) # 다른 앱에 있는 모델 연결시 'dojo.Tag'
    created_at = models.DateTimeField(auto_now_add = True) # 생성 될 떄, 자동 저장
    updated_at = models.DateTimeField(auto_now=True)       # 갱신 될 때, 자동 갱신
    # 기본 정렬 설정
    class Meta:
        ordering = ['-id']

    # 글 title 보이기
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now=True)   


class Tag(models.Model):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name




