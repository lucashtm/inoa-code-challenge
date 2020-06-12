from .month_map import MONTH_MAP
from django.utils import timezone
from django.db.models import Sum

class JsonExpensesChartData:
  def __init__(self, user, year=None, month=None):
    self.user = user
    self.month = MONTH_MAP.get(month) or timezone.now().month
    self.year = year or timezone.now().year
  
  def data(self):
    return (self.user.expense_set.filter(created_at__year=self.year, created_at__month=self.month)
                                 .order_by('created_at'))

  def group_by_day(self):
    days_values = {}
    for expense in self.data():
      day = expense.created_at.day
      if not days_values.get(day):
        days_values[day] = 0  
      days_values[day] += expense.value
    return days_values

  def render(self):
    labels = []
    values = []
    data = self.group_by_day()
    for day in data.keys():
      labels.append(self.day_to_label(day))
      values.append(data[day])
    data = {
      'labels': labels,
      'datasets': [{
        'data': values
      }]
    }
    return data

  def day_to_label(self, day):
    return f'{self.month}/{day}'