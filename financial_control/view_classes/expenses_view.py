from django.template import loader
from django.shortcuts import redirect, render
from django.utils import timezone

from financial_control.models import Expense
from financial_control.models import Category

from ..services.expenses_query import ExpensesQuery

class ExpensesView:
  def index(request):
    if request.user.is_authenticated:
      expenses = ExpensesQuery(request.user, month=timezone.now().month).fetch()
      context = {
        'expenses': list(expenses)
      }
      return render(request, 'financial_control/expenses/index.html', context)
    else:
      return redirect('sessions_new')

  def create(request):
    if request.user.is_authenticated:
      category = Category.objects.get(id=request.POST['category_id'])
      expense = Expense(description=request.POST['description'], created_at=timezone.now() ,category=category, user=request.user, value=request.POST['value'])
      expense.save()
      return redirect('expenses_index')
    return redirect('sessions_new')

  def new(request):
    if request.user.is_authenticated:
      template = loader.get_template('financial_control/expenses/new.html')
      categories = Category.objects.all()
      context = {
        'categories': categories
      }
      return render(request, 'financial_control/expenses/new.html', context)
    else:
      return redirect('sessions_new')