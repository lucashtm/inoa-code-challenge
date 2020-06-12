from django.urls import path

from . import views

urlpatterns = [
  path('', views.root, name='root'),
  path('signin/', views.sessions_new, name='sessions_new'),
  path('session/', views.sessions_create, name='sessions_create'),
  path('user/expenses/', views.expenses_index, name='expenses_index'),
  path('user/expenses/new', views.expenses_new, name='expenses_new'),
  path('user/expenses/create', views.expenses_create, name='expenses_create'),
  path('user/insights/', views.insights_index, name='insights_index')
]