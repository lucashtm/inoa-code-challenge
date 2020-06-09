from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

class SessionsView:
  def new(request):
    template = loader.get_template('financial_control/signin.html')
    return HttpResponse(template.render({}, request))

  def create(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('expenses_index')
    else:
      return redirect('sessions_new')