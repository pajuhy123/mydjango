# dojo/view.py
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    qs =  Post.objects.all()
    
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains = q)
    
    return render(request, 'blog/post_list.html',{'post_list': qs, 'q':q })

def post_detail(request, id):
    #try:
    #    post = Post.objects.get(id=id)
    #except Post.DoesNotExist:
    #   raise Http404
    post = get_object_or_404(Post,id=id)  #위에 4가지 코드를 1줄로!
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post)  # 이미 model 에 post.get_absolute_url 함수를 구현 -->post_detail 로 이동
    
    else:
        form = PostForm
    return render(request, 'blog/post_form.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수했습니다.')  
            return redirect(post)  # 이미 model 에 post.get_absolute_url 함수를 구현 -->post_detail 로 이동
    
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})
