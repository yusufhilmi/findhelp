from django.urls import path

from findhelp.helpticket import views


app_name = "helpticket"
urlpatterns = [
    path("listings/all", view=views.ticket_list_view, name='home'),
    path("listings/category/<pk>/", view=views.ticket_list_categorized_view, name='categorized'),
    path("create/", view=views.ticket_create_view, name='create-ticket'),
    path("my-listings/update/<pk>/", view=views.ticket_update_view, name='update-ticket'),
    path("my-listings/delete/<pk>/", view=views.ticket_delete_view, name='delete-ticket'),
    path("my-listings/", view=views.profile_ticket_list_view, name='profile')
    # path("tickets/", views.tickets_view, name='tickets'),
]
