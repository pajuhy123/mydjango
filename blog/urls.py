#blog/ url.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'), #url revrse 
                                                                          #를 사용한다면 view 가 역으로 url을 계산
                                                                          #url이 변경되어도 쉽게 대처 가능!
    ]