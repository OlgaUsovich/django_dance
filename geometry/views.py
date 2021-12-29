from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def get_rectangle_area(request, width, height):
    area = width * height
    return render(request, 'geometry/rectangle.html', context = locals())


def get_square_area(request, width):
    square_area = width ** 2
    return render(request, 'geometry/square.html', context = locals())


def get_circle_area(request, radius):
    circle_area = float(3.14) * (radius ** 2)
    return render(request, 'geometry/circle.html', context = locals())


def rectangle(request, width, height):
    return redirect(reverse('geometry:rectangle', kwargs={'width': width, 'height': height}))


def square(request, width):
    return redirect(reverse('geometry:square', kwargs={'width': width}))


def circle(request, radius):
    return redirect(reverse('geometry:circle', kwargs={'radius': radius}))
