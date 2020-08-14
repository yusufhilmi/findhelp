from django.urls import path

from findhelp.helpticket import views


app_name = "helpticket"
urlpatterns = [
    path("", view=views.ticket_list_view, name='home'),
    path("category/<pk>/", view=views.ticket_list_categorized_view, name='categorized'),
    path("gethelp/", view=views.ticket_create_view, name='create-ticket'),
    path("profile/helptickets/<pk>/update/", view=views.ticket_update_view, name='update-ticket'),
    path("profile/helptickets/<pk>/delete/", view=views.ticket_delete_view, name='delete-ticket'),
    path("profile/", view=views.profile_ticket_list_view, name='profile')
    # path("tickets/", views.tickets_view, name='tickets'),
]
