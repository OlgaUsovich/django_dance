from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

horo_marks = {'aries': {3: range(21, 32), 4: range(1, 21)},
              'taurus': {4: range(21, 31), 5: range(1, 21)},
              'gemini': {5: range(21, 32), 6: range(1, 22)},
              'cancer': {6: range(23, 31), 7: range(1, 23)},
              'leo': {7: range(23, 32), 8: range(1, 24)},
              'virgo': {8: range(24, 32), 9: range(1, 24)},
              'libra': {9: range(24, 31), 10: range(1, 24)},
              'scorpio': {10: range(24, 32), 11: range(1, 23)},
              'sagittarius': {11: range(23, 31), 12: range(1, 22)},
              'capricorn': {12: range(23, 32), 1: range(1, 21)},
              'aquarius': {1: range(21, 32), 2: range(1, 21)},
              'pisces': {2: range(21, 30), 3: range(1, 21)}}


types = {'fire': {'aries': 'Description Aries....',
                  'taurus': 'Description taurus....',
                  'gemini': 'Description gemini....'},
         'earth': {'cancer': 'Description cancer....',
                   'leo': 'Description leo....',
                   'virgo': 'Description virgo....'},
         'air': {'libra': 'Description libra....',
                 'scorpio': 'Description scorpio....',
                 'sagittarius': 'Description sagittarius....'},
         'water': {'capricorn': 'Description capricorn....',
                   'aquarius': 'Description aquarius....',
                   'pisces': 'Description pisces....'}}


def get_horo_mark(request, month, day):
    for j, i in horo_marks.items():
        for k, v in i.items():
            if month == k and day in i[k]:
                return HttpResponse(f'{j}')
    return HttpResponse('Введена неверная дата')


def show_horo_types(request):
    type_list = types.keys()
    return render(request, 'horoscope/types_list.html', context=locals())


def show_horo(request, type):
    horos = types[type]
    return render(request, 'horoscope/horo_list.html', context=locals())


def show_horo_detail(request, type, mark):
    info = types[type][mark]
    return render(request, 'horoscope/horo_detail.html', context=locals())

