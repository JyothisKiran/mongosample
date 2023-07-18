from django.contrib.auth.models import User
from rest_framework import serializers
from sample.models import Task


class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, querset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'task']