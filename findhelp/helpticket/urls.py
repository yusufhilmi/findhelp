from django.urls import path

from findhelp.helpticket import views


app_name = "helpticket"
urlpatterns = [
    path("", view=views.ticket_list_view, name='index'),
    path("gethelp/", view=views.ticket_create_view, name='create-ticket'),
    path("<pk>/update/", view=views.ticket_update_view, name='update-ticket'),
    path("<pk>/delete/", view=views.ticket_delete_view, name='delete-ticket'),
    # path("tickets/", views.tickets_view, name='tickets'),
]
