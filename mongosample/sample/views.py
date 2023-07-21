from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

# function based views


@api_view(['GET', 'POST'])
def tasklist(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        print(tasks)
        serializer = TaskSerializer(tasks, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def taskoperations(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class based Views


class TaskListView(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.filter(user=self.request.user)
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):
        print("post")
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def create(self, request,*validated_data, format=None):
    #     pass
    
    def perform_create(self, serializer):
        print("perform create")
        serializer.save(user=self.request.user)
   

class TaskOperationsView(APIView):
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


# GenericAPIView and  mixins


class TaskListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  


class TaskRetrieveUpdateDestroy(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
   
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

# Generic CBV's

class GenericCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class GenericRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


