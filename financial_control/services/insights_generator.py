from django.utils import timezone
from financial_control.models import Expense
from django.db.models import Max
from .month_map import MONTH_MAP

class InsightsGenerator:

  def __init__(self, user, month=None, year=None):
    self.user = user
    self.month = MONTH_MAP.get(month) or timezone.now().month
    self.year = year or timezone.now().year

  def expenses(self):
    return self.user.expense_set.filter(created_at__year=self.year, created_at__month=self.month)

  def greatest_expenses(self, limit=5):
    return self.expenses().order_by('-value')[:limit]

  def total(self):
    return sum(map(lambda e: e.value, self.expenses()))