from django.urls import path

from . import views

urlpatterns = [
  path('', views.root, name='root'),
  path('signin/', views.new_session, name='new_session'),
  path('session/', views.create_session, name='create_session'),
  path('user/expenses/', views.expenses_index, name='expenses_index')
]