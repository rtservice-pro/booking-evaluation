"""TODO 3 — Export a city catalogue summary as a JSON string."""
import json
import json
from rooms.models import Location, Room


def export_city_summary(city: str) -> str:
    if not isinstance(city, str) or not city.strip():
        raise ValueError("La ville doit être renseignée.")

    city = city.strip()
    location = Location.objects.filter(city__iexact=city).first()

    if location:
        city_name = location.city
    else:
        city_name = city

    rooms = Room.objects.filter(location__city__iexact=city)
    room_codes = sorted(room.code for room in rooms)
    total_capacity = sum(room.capacity for room in rooms)

    summary = {
        "city": city_name,
        "total_rooms": len(room_codes),
        "total_capacity": total_capacity,
        "room_codes": room_codes,
    }

    return json.dumps(summary)
