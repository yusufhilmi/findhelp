from django.db import models
from findhelp.users.models import User


class HelpTicket(models.Model):
    URGENCY = (
        ("urgent", "Urgent"),
        ("normal", "Normal"),
    )

    category = models.CharField(max_length=300, choices=URGENCY, default="urgent")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket_owner")
    city = models.CharField(max_length=100, default="Istanbul")
    description = models.CharField(max_length=200, blank=False)
    contact = models.CharField(max_length=150, blank=False, default="İletişim Bilgileri")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.owner.name) + ' :' + self.category + ' at ' + self.city
