class ExpensesGrouper:
  def __init__(self, expenses):
    self.expenses = expenses

  def by_month(self):
    grouped = {}
    for expense in self.expenses:
      month = expense.created_at.strftime("%B")
      if not grouped.get(month):
        grouped[month] = []
      grouped[month].append(expense)
    return grouped
