from django.db import models
from findhelp.users.models import User


class HelpCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class HelpTicket(models.Model):
    categories = models.ManyToManyField(HelpCategory, related_name="ticket_category")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket_owner")
    city = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    contact = models.CharField(max_length=150,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.owner.name) + ' :' + ' at ' + self.city
