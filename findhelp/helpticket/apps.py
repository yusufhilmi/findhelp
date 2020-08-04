from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HelpticketConfig(AppConfig):
    name = "findhelp.helpticket"
    verbose_name = _("Tickets")

    def ready(self):
        try:
            import findhelp.helpticket.signals  # noqa F401
        except ImportError:
            pass
