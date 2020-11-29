import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_view():
    assert reverse("helpticket:home") == "/help/listings/all"
    assert resolve("/help/listings/all").view_name == "helpticket:home"
