from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from findhelp.helpticket.models import HelpTicket

from itertools import chain


def index(request):
    return HttpResponse("Hello, world. You're at the helpticket index.")


# def tickets_view(request):
#     helptickets = HelpTicket.objects.filter(category="urgent")
#     # helptickets = "loo"
#     return render(request, 'helpticket/tickets.html', {
#         'helptickets': helptickets
#     })


# def add_ticket(request):
#     return render(request, 'helpticket/tickets.html')


class TicketList(ListView):
    # paginate_by = 1
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    def get_queryset(self):
        urgents = HelpTicket.objects.filter(category="urgent")
        normals = HelpTicket.objects.filter(category="normal")

        return list(chain(urgents, normals))


ticket_list_view = TicketList.as_view()
