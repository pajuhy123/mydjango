from django import forms
from .models import Post
from mydjango.widgets.naver_map_point_widget import NaverMapPointWidget

class PostForm(forms.ModelForm):
    #dummy = forms.CharField(widget =NaverMapPointWidget)

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat' : NaverMapPointWidget,
        }