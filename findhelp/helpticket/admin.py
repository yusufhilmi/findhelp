from django.contrib import admin
from findhelp.helpticket.models import HelpTicket
# Register your models here.


class HelpTicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(HelpTicket, HelpTicketAdmin)
