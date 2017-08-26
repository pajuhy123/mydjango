from django import forms
from django.views.generic import CreateView,ListView,DetailView, UpdateView,DeleteView
from .models import Post 
from django.core.urlresolvers import reverse_lazy

#prefetch방법 2
#클래스 기반 뷰 재정의
class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set','comment_set')

post_list =  PostListView.as_view()
'''
#prefetch 방법 1
post_list =  ListView.as_view(model=Post,
                              queryset=Post.objects.all().prefetch_related('tag_set','comment_set')
                              )
'''
#post_list =  ListView.as_view(model=Post, paginate_by =10)

post_detail = DetailView.as_view(model = Post)

'''
#blog/form.py  원래는 여기에다가 form 을 구현
class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm 
    # success_url ='/..' 원래는 이 것을 구현해야한다. 그러나 get_absolute_url이 대신해주고 코드를 간편하게 해준다.

post_new = PostCreateView.as_view()
'''
post_new = CreateView.as_view(model =Post)
post_edit = UpdateView.as_view(model =Post, fields='__all__')

post_delete = DeleteView.as_view(model =Post, success_url= reverse_lazy('blog:post_list'))

