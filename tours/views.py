from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.views import View
from tours.models import departures
from tours.models import tours


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')


class DepartureView(View):
    def get(self, request, departure):
        if departure not in departures:
            raise Http404
        context = {
            "departure": departures[departure]
        }
        return render(request, "departure.html", context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404
        context = {
            "tour": tours[id]
        }
        return render(request, "tour.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<center><h2>Ой, что то сломалось... Простите извините!</h2></center>')


def custom_handler500(request):
    return HttpResponseServerError('Внутрення ошибка сервера')
