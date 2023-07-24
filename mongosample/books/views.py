# from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer, BookHLSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

# Create your views here.


@api_view(['POST', 'GET'])
def booklist(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET', 'PUT', 'DELETE'])
def bookoperations(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Booklist(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookHLSerializer

    # we can customise list, retrieve, put, destroy and create functions as per need


class BooklistRO(viewsets.ReadOnlyModelViewSet):

    # only list and retrieve methods are available

    queryset = Book.objects.all()
    serializer_class = BookHLSerializer

    def retrieve(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookHLSerializer(book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
