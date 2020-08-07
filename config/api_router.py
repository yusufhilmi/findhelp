from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from findhelp.users.api.views import UserViewSet
from findhelp.helpticket.api.views import HelpTicketViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("helpticket", HelpTicketViewSet)

app_name = "api"
urlpatterns = router.urls
