from dataclasses import fields
from rest_framework import serializers
from .models import Selection


class SelectionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        query = "INSERT INTO selection_selection (event_id, price, outcome, active, name)" \
                f"VALUES ('{validated_data['event'].id}', '{validated_data['price']}', " \
                f"'{validated_data['outcome']}', {validated_data['active']}, "\
                f"'{validated_data['name']}') returning *"
        return Selection.objects.raw(query)[0]

    class Meta:
        model = Selection
        fields = '__all__'
    