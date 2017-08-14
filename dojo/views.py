#dojo/view.py
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

def post_detail(request, id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'dojo/post_detail.html',{
      'post':post,
})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit =False) #save 함수 호출을 지연시킨다. 
            post.ip = request.META['REMOTE_ADDR']  #ip 얻어오기
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) #순서!
        if form.is_valid():
            #방법 1
            '''
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            '''
            #방법 2
            '''
            post = Post(title=form.cleaned_data['title'], 
                        content=form.cleaned_data['content'])
            post.save()
            '''
            #방법 3
            '''
            post = Post.objects.create(title=title=form.cleaned_data['title'],
                                      content=form.cleaned_data['content'])
            '''
            #방법 4
            '''
            post = Post.objects.create(**form.cleaned_data)
            '''
            #방법 5 --> forms.py에 save 함수 구현
            post = form.save(commit =False) #save 함수 호출을 지연시킨다. 
            post.ip = request.META['REMOTE_ADDR']  #ip 얻어오기
            post.save()

            return redirect('/dojo/')
    else:
        form = PostForm
    return render(request, 'dojo/post_form.html', { 'form':form, })

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




