from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import JsonResponse

from ..services.insights_generator import InsightsGenerator

def insights_index(request):
  if request.user.is_authenticated:
    year = request.GET.get('year')
    month = request.GET.get('month')
    insights_generator = InsightsGenerator(request.user, month=month, year=year)
    context = {
      'month': month,
      'total': insights_generator.total(),
      'greatest_expenses': insights_generator.greatest_expenses()
    }
    return render(request, 'financial_control/insights/index.html', context)
  return redirect('sessions_new')

def insights_ajax_expenses(request):
  return JsonResponse({ 'a': 2 })