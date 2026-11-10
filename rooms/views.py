"""TODO 2 — Read-only rooms endpoint with an optional city filter."""
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_queryset(self):
        rooms = Room.objects.all().order_by("code")
        city = self.request.query_params.get("city")

        if city is not None:
            city = city.strip()
            if not city:
                raise ValidationError({"city": "Ce champ ne peut pas être vide."})
            rooms = rooms.filter(location__city__iexact=city)

        return rooms
