from django.db import models


class HelpTicket(models.Model):
    description = models.CharField(max_length=200)
