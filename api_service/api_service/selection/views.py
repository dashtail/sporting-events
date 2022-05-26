from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_service.commons.helpers import get_update_query_by_id, check_actives_events
from .serializers import SelectionSerializer
from .models import Selection


class SelectionView(APIView):
    def post(self, request):
        """
        create a new selection
        """
        serializer = SelectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        return all selections
        """
        selections = Selection.objects.raw(
            'SELECT id, name, event_id, price, outcome, active FROM selection_selection')
        serializer = SelectionSerializer(selections, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            selection = Selection.objects.raw(
                'SELECT id, name, event_id, price, outcome, active '
                f'FROM selection_selection WHERE id = {id}'
            )[0]
        except:
            raise Http404

        data = request.data
        if data:
            query = get_update_query_by_id(id, data, 'selection_selection')
            selection_updated = Selection.objects.raw(query)
            serializer = SelectionSerializer(selection_updated[0])

            if "active" in data:
                if not data['active']:
                    check_actives_events.apply_async(
                        args=[selection.event.id]
                    )

        return Response(serializer.data)
