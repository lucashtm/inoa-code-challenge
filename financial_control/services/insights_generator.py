from django.utils import timezone
from financial_control.models import Expense
from django.db.models import Max

class InsightsGenerator:
  MONTH_MAP = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
  }

  def __init__(self, user, month=None, year=None):
    self.user = user
    self.month = self.__class__.MONTH_MAP.get(month) or timezone.now().month
    self.year = year or timezone.now().year

  def expenses(self):
    return self.user.expense_set.filter(created_at__year=self.year, created_at__month=self.month)

  def greatest_expenses(self, limit=5):
    return self.expenses().order_by('-value')[:limit]

  def total(self):
    return sum(map(lambda e: e.value, self.expenses()))