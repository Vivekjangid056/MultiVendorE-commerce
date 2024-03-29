from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method == 'POST':    
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been registered sucessfully ')
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registeruser.html', context)
