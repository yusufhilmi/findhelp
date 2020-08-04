from django.urls import path

from findhelp.helpticket import views


app_name = "helpticket"
urlpatterns = [
    path("", views.index, name='index'),
    path("tickets/", views.tickets_view, name='tickets'),
]
