from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import JsonResponse

from ..services.insights_generator import InsightsGenerator
from ..services.json_expenses_chart_data import JsonExpensesChartData

def insights_index(request):
  if request.user.is_authenticated:
    year = request.GET.get('year')
    month = request.GET.get('month')
    insights_generator = InsightsGenerator(request.user, month=month, year=year)
    context = {
      'user_logged_in': True,
      'month': month,
      'total': insights_generator.total(),
      'greatest_expenses': insights_generator.greatest_expenses()
    }
    return render(request, 'financial_control/insights/index.html', context)
  return redirect('sessions_new')

def insights_ajax_expenses(request):
  if request.user.is_authenticated:
    year = request.GET.get('year')
    month = request.GET.get('month')
    data = JsonExpensesChartData(request.user, month=month, year=year).render()
    return JsonResponse(data)
  return JsonResponse({'error': 'Forbidden'}, status=403)