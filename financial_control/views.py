from django.template import loader
from django.http import HttpResponse

from .view_classes.sessions_view import SessionsView
from .view_classes.expenses_view import ExpensesView

# Create your views here.
def root(request):
  template = loader.get_template('financial_control/root.html')
  return HttpResponse(template.render({}, request))

def new_session(request):
  return SessionsView.new(request)

def create_session(request):
  return SessionsView.create(request)

def expenses_index(request):
  return ExpensesView.index(request)