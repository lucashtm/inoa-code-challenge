from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse

class ExpensesView:
  def index(request):
    if request.user.is_authenticated:
      template = loader.get_template('financial_control/expenses_index.html')
      return HttpResponse(template.render({}, request))
    else:
      return redirect('new_session')