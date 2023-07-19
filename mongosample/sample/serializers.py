from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['user', 'name', 'description', 'date', 'completed']
