from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_service.commons.helpers import get_update_query_by_id
from .serializers import SportSerializer
from .models import Sport


class SportView(APIView):
    def post(self, request):
        """
        create a new sport
        """
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        return all sports or filtered sports
        """
        sports = Sport.objects.raw(
            'SELECT id, name, slug, active FROM sport_sport')

        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            event = Sport.objects.raw(
                f'SELECT id FROM sport_sport WHERE id = {id}'
            )[0]
        except:
            raise Http404

        data = request.data
        if data:
            query = get_update_query_by_id(id, data, 'sport_sport')
            event_updated = Sport.objects.raw(query)
            serializer = SportSerializer(event_updated[0])

        return Response(serializer.data)