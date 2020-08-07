# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from itertools import chain


from findhelp.helpticket.models import HelpTicket
from findhelp.users.models import User


class TicketList(ListView):
    # paginate_by = 1
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    def get_context_data(self, **kwargs):
        context = super(TicketList, self).get_context_data(**kwargs)
        context['normalhelptickets'] = HelpTicket.objects.filter(category="normal")

        return context

    def get_queryset(self):
        urgents = HelpTicket.objects.filter(category="urgent")

        return urgents


ticket_list_view = TicketList.as_view()


class TicketCreate(CreateView):
    model = HelpTicket
    fields = ['category', 'city', 'description', 'contact']

    def form_valid(self, form):
        form.instance.owner = User.objects.get(username=self.request.user)
        return super(TicketCreate, self).form_valid(form)


ticket_create_view = TicketCreate.as_view(success_url="/helpticket/")


class TicketUpdate(UpdateView):
    model = HelpTicket
    fields = ['category', 'city', 'description', 'contact']
    success_url = "/helpticket/"


ticket_update_view = TicketUpdate.as_view()


class TicketDelete(DeleteView):
    model = HelpTicket
    success_url = "/helpticket/"


ticket_delete_view = TicketDelete.as_view()
