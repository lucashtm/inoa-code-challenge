from .month_map import MONTH_MAP
from django.utils import timezone
from django.db.models.functions import TruncDay
from django.db.models import Sum

class JsonExpensesChartData:
  def __init__(self, user, year=None, month=None):
    self.user = user
    self.month = MONTH_MAP.get(month) or timezone.now().month
    self.year = year or timezone.now().year
  
  def data(self):
    return (self.user.expense_set.filter(created_at__year=self.year, created_at__month=self.month)
                                 .order_by('created_at')
                                 .annotate(day=TruncDay('created_at'))
                                 .values('day')
                                 .annotate(s=Sum('value')))

  def render(self):
    labels = []
    values = []
    for entry in self.data():
      labels.append(self.data_to_label(entry['day']))
      values.append(entry['s'])
    data = {
      'labels': labels,
      'datasets': [{
        'data': values
      }]
    }
    return data

  def data_to_label(self, data):
    return f'{data.month}/{data.day}'