#dojo/view.py
from django.http import HttpResponse
from django.shortcuts import render


def mysum(request,numbers):   
    #numbers=1/2/3/4/324//234//23/4/234/
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s:int(s or 0), numbers.split("/"))) # url에 // 들어갔을 때, 대비

    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요 {}님, {}살이시네요'.format(name,age))


