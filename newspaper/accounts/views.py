from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm
# Create your views here.

class SignUp(CreateView):
    nodel = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
