from rest_framework import viewsets  # , permissions

from findhelp.helpticket.api.serializers import HelpTicketSerializer
from findhelp.helpticket.api.permissions import IsOwnerOrReadOnly
from findhelp.helpticket.models import HelpTicket


class HelpTicketViewSet(viewsets.ModelViewSet):
    queryset = HelpTicket.objects.all()
    serializer_class = HelpTicketSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
