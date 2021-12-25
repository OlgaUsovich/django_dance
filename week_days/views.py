from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def get_day_by_num(request, day_num):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day_num-1 in range(len(days)):
        return redirect(reverse('week_days:days_by_name', kwargs={'day_name': days[day_num-1]}))
    else:
        return HttpResponse(f'Неверный номер дня - {day_num}')


def get_day_by_name(request, day_name):
    day_names = {'monday': 'Monday is the 1st day of the week',
                 'tuesday': 'Tuesday is the 2d day of the week',
                 'wednesday': 'Wednesday is the 3d day of the week',
                 'thursday': 'Thursday is the 4th day of the week',
                 'friday': 'Friday is the 5th day of the week',
                 'saturday': 'Saturday is the 6th day of the week and the 1st day of weekends',
                 'sunday': 'Sunday is the last day of the week and the last day of weekends'}
    return HttpResponse(f'{day_names[day_name]}')


def show_greeting(request):
    return render(request, 'week_days/greeting.html')

