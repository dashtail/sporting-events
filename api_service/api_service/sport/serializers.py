from rest_framework import serializers
from django.db import connection
from .models import *


class SportSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        query = "INSERT INTO sport_sport (name, slug, active) VALUES" \
                f"('{validated_data['name']}', '{validated_data['slug']}', " \
                f"{validated_data['active']}) returning *"

        return Sport.objects.raw(query)[0]

    class Meta:
        model = Sport
        fields = '__all__'
