from django import forms

from findhelp.helpticket.models import HelpTicket


class HelpTicketForm(forms.ModelForm):
    class Meta:
        model = HelpTicket
        fields = ['category', 'city', 'description', 'contact']
