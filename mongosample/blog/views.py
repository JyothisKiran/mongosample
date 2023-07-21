from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import EntrySerializer
from .models import Entry

# Create your views here.


class EntryListView(APIView):
    
    def get(self, request):
        queryset = Entry.objects.all()
        serializer = EntrySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = EntrySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EntryOperationsView(APIView):

    def get_object(self, pk):
        try:
            obj = Entry.objects.get(pk=pk)
            return obj
        except Entry.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       

    def get(self, request, pk):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        return Response(serializer.data)

    def put(self, request, pk):
        entry = self.get_object(pk)
        serializer = EntrySerializer(entry)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        entry = self.get_object(pk)
        entry.delete()
        return Response(status=status.HTTP_404_NOT_FOUND) 