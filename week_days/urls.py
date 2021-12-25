from django.urls import path

from week_days import views

app_name = 'week_days'

urlpatterns = [
    path('', views.show_greeting),
    path('todo_week/<int:day_num>/', views.get_day_by_num, name='days_by_num'),
    path('todo_week/<slug:day_name>/', views.get_day_by_name, name='days_by_name'),

]