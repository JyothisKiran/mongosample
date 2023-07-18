from django.urls import path
from .views import tasklist, taskoperations
from .views import TaskListView, TaskOperationsView
from .views import TaskRetrieveUpdateDestroy, TaskListCreateView
from .views import GenericCreateView, GenericRetriveUpdateDestroyView

urlpatterns = [
    path('list/',tasklist,name='task_list'),
    path('operations/<int:pk>/',taskoperations,name='task_operations'),
    path('list_cbv/',TaskListView.as_view(),name='task_list_cbv'),
    path('operations_cbv/<int:pk>/',TaskOperationsView.as_view(),name='task_operations_cbv'),
    path('list_generic/',TaskListCreateView.as_view(),name='task_list_generic'),
    path('operations_generic/<int:pk>/',TaskRetrieveUpdateDestroy.as_view(),name='operations_generic'),
    path('list_generic_cbv/',GenericCreateView.as_view(),name='task_list_genericcbv'),
    path('operations_generic_cbv/<int:pk>/',GenericRetriveUpdateDestroyView.as_view(),name='operations_genericcbv'),
]