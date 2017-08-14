#blog/ url.py
from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns=[
    url(r'^$',views_cbv.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'), #url revrse를 사용한다면 view 가 역으로 url을 계산 url이 변경되어도 쉽게 대처 가능!
            
    url(r'^new/$', views.post_new, name='post_new'),   
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^cbv/new/$', views_cbv.post_new),                                                     
    ]