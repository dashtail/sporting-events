from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        query = "INSERT INTO event_event (sport_id, type, slug, active, name, status," \
                "scheduled_start, actual_start) VALUES (" \
                f"'{validated_data['sport'].id}', '{validated_data['type']}', " \
                f"'{validated_data['slug']}', {validated_data['active']}, "\
                f"'{validated_data['name']}','{validated_data['status']}',"\
                f"'{validated_data['scheduled_start']}'," \
                f"'{validated_data['actual_start']}') returning *"
        return Event.objects.raw(query)[0]

    class Meta:
        fields = '__all__'
        model = Event