from django.urls import path

from . import views

urlpatterns = [
  path('', views.root, name='root'),
  path('signin/', views.sessions_new, name='sessions_new'),
  path('session/', views.sessions_create, name='sessions_create'),
  path('session/delete', views.sessions_delete, name='sessions_delete'),
  path('user/expenses/', views.expenses_index, name='expenses_index'),
  path('user/expenses/new', views.expenses_new, name='expenses_new'),
  path('user/expenses/create', views.expenses_create, name='expenses_create'),
  path('user/expenses/<int:expense_id>/delete', views.expenses_delete, name='expenses_delete'),
  path('user/insights/', views.insights_index, name='insights_index'),
  path('user/insights/expenses', views.insights_ajax_expenses, name='insights_ajax_expenses')
]