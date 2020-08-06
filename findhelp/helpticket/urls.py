from django.urls import path

from findhelp.helpticket import views


app_name = "helpticket"
urlpatterns = [
    path("", view=views.ticket_list_view, name='index'),
    path("gethelp/", views.add_ticket, name='gethelp'),
    # path("tickets/", views.tickets_view, name='tickets'),
]
