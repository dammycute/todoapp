from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TodoApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields  = ["id", "title", "desc", "is_complete"]
    search_fields  = ["id", "title", "desc", "is_complete"]
    ordering_fields  = ["id", "title", "desc", "is_complete"]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
    
    

class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
    