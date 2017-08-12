from django import forms
from django.views.generic import CreateView
from .models import Post


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
