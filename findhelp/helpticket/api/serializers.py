from rest_framework import serializers

from findhelp.helpticket.models import HelpTicket


class HelpTicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = HelpTicket
        fields = ['owner', 'category', 'city', 'description', 'contact']

        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        # }
