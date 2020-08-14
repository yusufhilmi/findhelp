from django.shortcuts import reverse
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# from itertools import chain
from datetime import timedelta
from django.utils import timezone

from findhelp.helpticket.models import HelpTicket, HelpCategory
from findhelp.users.models import User

PAGINATION = 8


class TicketList(ListView):
    paginate_by = PAGINATION
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    def get_context_data(self, **kwargs):
        """
            Add other things to the context
        """
        context = super(TicketList, self).get_context_data(**kwargs)
        context['categories'] = HelpCategory.objects.all()
        return context

    def get_queryset(self):
        time_threshold = timezone.now() - timedelta(days=30)
        helptickets = HelpTicket.objects.filter(updated_at__gt=time_threshold)

        return helptickets


ticket_list_view = TicketList.as_view()


class TicketListCategorized(ListView):
    paginate_by = PAGINATION
    template_name = 'helpticket/tickets.html'
    context_object_name = 'helptickets'

    def get_queryset(self):
        time_threshold = timezone.now() - timedelta(days=30)
        helptickets = HelpTicket.objects.filter(categories=self.kwargs["pk"], updated_at__gt=time_threshold)

        return helptickets


ticket_list_categorized_view = TicketListCategorized.as_view()


class TicketCreate(LoginRequiredMixin, CreateView):
    model = HelpTicket
    fields = ['categories', 'city', 'description', 'contact']

    def form_valid(self, form):
        form.instance.owner = User.objects.get(username=self.request.user)
        return super(TicketCreate, self).form_valid(form)


ticket_create_view = TicketCreate.as_view(success_url="/")


class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = HelpTicket
    fields = ['categories', 'city', 'description', 'contact']
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
    paginate_by = PAGINATION
    template_name = 'helpticket/profile.html'
    context_object_name = 'helptickets'

    def get_queryset(self):
        helptickets = HelpTicket.objects.filter(owner=self.request.user)

        return helptickets


profile_ticket_list_view = ProfileTicketList.as_view()
