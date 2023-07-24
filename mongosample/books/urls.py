from django.urls import path, include
from .views import booklist, bookoperations
from .views import Booklist, BooklistRO, ListOfBooks
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'list', Booklist)
router.register(r'rolist', BooklistRO)
router.register(r'genericlist', ListOfBooks, basename='book-list')

urlpatterns = [
    path('list/', booklist, name='book-list'),
    path('oper/<int:pk>/', bookoperations, name='book-oper'),
    path('route/', include(router.urls)),
]
