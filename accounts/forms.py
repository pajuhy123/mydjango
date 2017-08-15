from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # class Meta() 와 사용 하면 , 디폴트 필드를 다 없애므로 오류가 난가 , 즉 상속을 이용해 사용해야한다.
         fields = UserCreationForm.Meta.fields + ('email',)  