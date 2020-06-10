from django.utils import timezone
from .expenses_grouper import ExpensesGrouper
from financial_control.models import Expense

class ExpensesQuery:

  def __init__(self, user, periodicity='month'):
    self.user = user
    self.periodicity = periodicity
    self.query_hash = { 'month': self.month, 'year': self.year }

  def fetch(self):
    expenses = self.query_hash[self.periodicity]()
    return ExpensesGrouper(expenses).by_month()

  def month(self):
    return self.user.expense_set.filter(created_at__year=timezone.now().year, created_at__month=timezone.now().month).order_by('-created_at')

  def year(self):
    return self.user.expense_set.filter(created_at__year=timezone.now().year).order_by('-created_at')

  