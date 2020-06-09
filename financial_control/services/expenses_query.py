from django.utils import timezone
from financial_control.models import Expense

class ExpensesQuery:

  def __init__(self, user, year=timezone.now().year, month=None):
    self.user = user
    self.year = year
    self.month = month

  def fetch(self):
    return self.query()

  def query(self):
    if self.month:
      return self.monthly()
    return self.yearly()

  def monthly(self):
    return self.user.expense_set.filter(created_at__year=self.year, created_at__month=self.month)

  def yearly(self):
    return self.user.expense_set.filter(created_at__year=self.year)