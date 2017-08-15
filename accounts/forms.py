from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):  # class Meta() 와 사용 하면 , 디폴트 필드를 다 없애므로 오류가 난가 , 즉 상속을 이용해 사용해야한다.
         fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()  
        profile = Profile.objects.create(
           user = user,
           phone_number = self.cleaned_data['phone_number'],
           address = self.cleaned_data['address'])
        return user