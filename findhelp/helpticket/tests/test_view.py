import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_view():

    assert reverse("helpticket:index") == "/helpticket/"
    assert resolve("/helpticket/").view_name == "helpticket:index"
