from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MetaTest
from .serializers import MetaTestCreationSerializer
from rest_framework import permissions
# Create your views here.
class MetaTestList(ListCreateAPIView):

    serializer_class = MetaTestCreationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def get_queryset(self):
        return MetaTest.objects.all()
