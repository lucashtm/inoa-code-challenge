from django.template import loader
from django.http import HttpResponse

def root(request):
  template = loader.get_template('financial_control/root.html')
  context = {
    'user_logged_in': request.user.is_authenticated
  }
  return HttpResponse(template.render(context, request))