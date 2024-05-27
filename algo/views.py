from .predict import predict
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

class AIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        map=request.data.get('map')
        pd=predict(map)
        return Response({'data':pd},status=status.HTTP_200_OK)

