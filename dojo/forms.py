#dojo/forms.py
from django import forms
from .models import Post
'''
#원래는 models.py에 둔다.
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3 글자 이상 입력해 주세요')
'''

class PostForm(forms.ModelForm):  # 장고 폼은 PostForm(forms.Form)
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'content']


    '''
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget = forms.Textarea)
    '''
    '''
    #모델 폼에는 내부적으로 해당 모델 인스턴스로 저장을 지원
    def save(self, commit=True):
        post = Post(**self.cleaned_data)  #post ->self.instance
        if commit:
            post.save()
        return post
    '''