from .models import Profile
from django.shortcuts import redirect, render
from .forms import Register
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def index(request):
   return render(request, 'pages/home.html')
def register(request):
   form = Register()
   if request.method == 'POST':
          form = Register(request.POST)
          if form.is_valid():
                 form.save()
                 return HttpResponseRedirect('/login')
   return render(request, 'pages/register.html', {'form' : form})

@login_required
def profile(request):
   return render(request, 'pages/profile.html')

@login_required
def profileupdate(request):
   if request.method == 'POST':
      u_form = UserUpdateForm(request.POST,instance=request.user)
      p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
      if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         return redirect('/profile')
   else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfileUpdateForm(instance=request.user.profile)
   context = {
      'u_form': u_form,
      'p_form': p_form
   }
   return render(request, 'pages/updatep.html',context)