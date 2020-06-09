from django.template import loader
from django.shortcuts import redirect, render
from django.utils import timezone

from financial_control.models import Expense
from financial_control.models import Category

class ExpensesView:
  def index(request):
    if request.user.is_authenticated:
      return render(request, 'financial_control/expenses/index.html', {})
    else:
      return redirect('sessions_new')

  def create(request):
    if request.user.is_authenticated:
      expense = Expense(description=request.POST['description'], created_at=timezone.now() ,category_id=request.POST['category_id'], user_id=request.user.id)
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