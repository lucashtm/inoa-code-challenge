from django.template import loader
from django.shortcuts import redirect, render
from django.utils import timezone

from financial_control.models import Expense
from financial_control.models import Category

from ..services.expenses_query import ExpensesQuery

def expenses_index(request):
  if request.user.is_authenticated:
    periodicity = request.GET.get('periodicity') or 'month'
    expenses = ExpensesQuery(request.user, periodicity=periodicity).fetch()
    context = {
      'user_logged_in': True,
      'months': expenses.keys(),
      'expenses': expenses
    }
    return render(request, 'financial_control/expenses/index.html', context)
  else:
    return redirect('sessions_new')

def expenses_new(request):
  if request.user.is_authenticated:
    categories = Category.objects.all()
    context = {
      'categories': categories
    }
    return render(request, 'financial_control/expenses/new.html', context)
  else:
    return redirect('sessions_new')

def expenses_create(request):
  if request.user.is_authenticated:
    category = Category.objects.get(id=request.POST['category_id'])
    expense = Expense(description=request.POST['description'], created_at=timezone.now() ,category=category, user=request.user, value=request.POST['value'])
    expense.save()
    return redirect('expenses_index')
  return redirect('sessions_new')