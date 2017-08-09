#dojo/view.py
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def mysum(request,numbers):   
    #numbers=1/2/3/4/324//234//23/4/234/
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s:int(s or 0), numbers.split("/"))) # url에 // 들어갔을 때, 대비

    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요 {}님, {}살이시네요'.format(name,age))

def post_list1(request):
    name ='공유'
    return HttpResponse('''
        <h1>Askdjango</h1>
        <p>{name}</p>
        <p> 파이썬 열심히 공부해서 웹 개발을 할 수 있도록 하자!</p>'''.format(name=name))

def post_list2(request):
    name='공유'
    return render(request, 'dojo/post_list.html', {'name': name})

def post_list3(request):
    return JsonResponse({
           'message': '안녕 파이썬&장고',
           'items' :['파이썬', '장고', 'Celery','Azure','AWS'],
           }, json_dumps_params={'ensure_ascii':False})

def excel_download(request):
    #filepath = '/Users/joon/mydjango/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR,'gdplev.xls')

    filename = os.path.basename(filepath)
    with open(filepath , 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') #디폴트로 text.html 되어있다. 
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response




