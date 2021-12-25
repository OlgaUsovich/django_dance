from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника равна: {width*height}')


def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата равна: {width**2}')


def get_circle_area(request, radius):
    return HttpResponse(f'Площадь круга равна: {float(3.14)*(radius**2)}')


def rectangle(request, width, height):
    return redirect(reverse('geometry:rectangle', kwargs={'width': width, 'height': height}))


def square(request, width):
    return redirect(reverse('geometry:square', kwargs={'width': width}))


def circle(request, radius):
    return redirect(reverse('geometry:circle', kwargs={'radius': radius}))
