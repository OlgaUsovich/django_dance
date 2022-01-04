from django.urls import path

from horoscope import views

app_name = 'horoscope'

urlpatterns = [
    path('<int:month>/<int:day>/', views.get_horo_mark),
    path('type/', views.show_horo_types),
    path('type/<str:type>/', views.show_horo, name='show_horo'),
    path('type/<str:type>/<str:mark>/', views.show_horo_detail, name='show_horo_detail'),

]