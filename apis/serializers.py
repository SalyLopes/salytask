from rest_framework import serializers
from tasks import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'item',
            'status',
        )
        model = models.Task