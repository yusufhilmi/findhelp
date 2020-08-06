import pytest
from django.urls import reverse  # , resolve #


pytestmark = pytest.mark.django_db


def test_view():

    assert reverse("helpticket:tickets") == "/helpticket/tickets/"
    # assert resolve("/helpticket/tickets/").view_name == "helpticket:tickets_view"

