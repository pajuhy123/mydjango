#dojo/ url.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),  #123/123/12312/123/ ..모두적용
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),
]