from django.urls import path
from .views import EntryListView, EntryOperationsView

urlpatterns = [
    path('list/', EntryListView.as_view(), name='entry-list'),
    path('oper/<int:pk>/', EntryOperationsView.as_view(), name='entry-oper'),
]