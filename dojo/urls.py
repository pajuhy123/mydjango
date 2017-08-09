#dojo/ url.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),  #123/123/12312/123/ ..모두적용
]