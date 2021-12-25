from django.urls import path

from horoscope import views

app_name = 'horoscope'

urlpatterns = [
    path('<int:month>/<int:day>/', views.get_horo_mark),
]