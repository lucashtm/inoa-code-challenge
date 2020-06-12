from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.template import loader

def sessions_new(request):
  return render(request, 'financial_control/signin.html', {})

def sessions_create(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return redirect('expenses_index')
  else:
    return redirect('sessions_new')