#account/views.py
from django.conf import settings
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm   # for 회원가입 cumstom 화

def signup(request):
    if request.method =='POST':
         form = SignupForm(request.POST)
         if form.is_valid():
             user = form.save()
             return redirect(settings.LOGIN_URL)  #default : "/account/login"
    else:
            form = SignupForm()
    return render(request, "accounts/signup_form.html", {
          'form' : form,
      })
    
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
    