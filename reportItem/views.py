from django.shortcuts import render
from report.serializers import ReportCreationSerializer
from report.models import Report
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import ReportItemCreationSerializer
from rest_framework import permissions
from rest_framework import status

class RequestCreationView(GenericAPIView):
    serializer_class1 = ReportItemCreationSerializer
    serializer_class = ReportCreationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        serializer=self.serializer_class
        owner=request.user
        report=Report(
            owner=owner
        )
        report.save()
        map=request.data.get('map')
        for key in map.keys():
            serializer=self.serializer_class1()
            # value,test_name,report
            reportItem=serializer.create(value=map[key],test_name=key,report=report)
        return Response({'message':"Successfully saved"},status=status.HTTP_200_OK)

