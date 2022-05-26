from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_service.commons.helpers import get_update_query_by_id, check_actives_sports
from .serializers import EventSerializer
from .models import Event


class EventView(APIView):
    def post(self, request):
        """
        create a new event
        """
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        return all events
        """
        events = Event.objects.raw(
            'SELECT id, name, slug, type, sport_id, status,'
            'scheduled_start, actual_start, active FROM event_event')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            event = Event.objects.raw(
                f'SELECT id FROM event_event WHERE id = {id}'
            )[0]
        except:
            raise Http404

        data = request.data
        if data:
            query = get_update_query_by_id(id, data, 'event_event')
            event_updated = Event.objects.raw(query)
            serializer = EventSerializer(event_updated[0])

            if "active" in data:
                if not data['active']:
                    check_actives_sports.apply_async(
                        args=[event.sport.id]
                    )

        return Response(serializer.data)
