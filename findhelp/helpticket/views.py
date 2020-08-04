from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the helpticket index.")


def tickets_view(request):
    return render(request, 'helpticket/tickets.html')
