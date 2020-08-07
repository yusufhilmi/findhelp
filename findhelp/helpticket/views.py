from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from itertools import chain
from django.urls import reverse
from findhelp.helpticket.models import HelpTicket
from findhelp.helpticket.forms import HelpTicketForm


def index(request):
    return HttpResponse("Hello, world. You're at the helpticket index.")


# def tickets_view(request):
#     helptickets = HelpTicket.objects.filter(category="urgent")
#     # helptickets = "loo"
#     return render(request, 'helpticket/tickets.html', {
#         'helptickets': helptickets
#     })


def add_ticket(request):
    form = HelpTicketForm()
    return render(request, 'helpticket/create_ticket.html', {
        'help_form': form
    })


class TicketCreate(CreateView):
    model = HelpTicket
    fields = ['owner', 'category', 'city', 'description', 'contact']


ticket_create_view = TicketCreate.as_view(success_url="/helpticket/")


class TicketList(ListView):
    # paginate_by = 1
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    def get_queryset(self):
        urgents = HelpTicket.objects.filter(category="urgent")
        normals = HelpTicket.objects.filter(category="normal")

        return list(chain(urgents, normals))


ticket_list_view = TicketList.as_view()
