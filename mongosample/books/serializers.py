from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ["user", 'name', 'description']


class BookHLSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['url', 'user', 'name', 'description']
