# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from itertools import chain
from datetime import timedelta
from django.utils import timezone

from findhelp.helpticket.models import HelpTicket
from findhelp.users.models import User


class TicketList(ListView):
    paginate_by = 50
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    # def get_context_data(self, **kwargs):
    #   """"
    #       Add other things to the context
    #   """"
    #     context = super(TicketList, self).get_context_data(**kwargs)
    #     context['normalhelptickets'] = HelpTicket.objects.filter(category="normal")
    #     return context

    def get_queryset(self):
        time_threshold = timezone.now() - timedelta(days=30)
        urgents = HelpTicket.objects.filter(category="urgent", updated_at__gt=time_threshold)
        normals = HelpTicket.objects.filter(category="normal", updated_at__gt=time_threshold)

        return list(chain(urgents, normals))


ticket_list_view = TicketList.as_view()


class TicketCreate(LoginRequiredMixin, CreateView):
    model = HelpTicket
    fields = ['category', 'city', 'description', 'contact']

    def form_valid(self, form):
        form.instance.owner = User.objects.get(username=self.request.user)
        return super(TicketCreate, self).form_valid(form)


ticket_create_view = TicketCreate.as_view(success_url="/")


class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = HelpTicket
    fields = ['category', 'city', 'description', 'contact']
    success_url = "/"

    def get_object(self, *args, **kwargs):
        obj = super(TicketUpdate, self).get_object(*args, **kwargs)
        if not obj.owner == self.request.user:
            raise PermissionDenied
        return obj


ticket_update_view = TicketUpdate.as_view()


class TicketDelete(LoginRequiredMixin, DeleteView):
    model = HelpTicket
    success_url = "/"

    def get_object(self, *args, **kwargs):
        obj = super(TicketDelete, self).get_object(*args, **kwargs)
        if not obj.owner == self.request.user:
            raise PermissionDenied
        return obj


ticket_delete_view = TicketDelete.as_view()


class ProfileTicketList(LoginRequiredMixin, ListView):
    paginate_by = 20
    template_name = 'helpticket/profile.html'
    context_object_name = 'helptickets'

    def get_queryset(self):
        urgents = HelpTicket.objects.filter(category="urgent", owner=self.request.user)
        normals = HelpTicket.objects.filter(category="normal", owner=self.request.user)

        return list(chain(urgents, normals))


profile_ticket_list_view = ProfileTicketList.as_view()
