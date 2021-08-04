from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import UserProfile
from .serializer import UserSerializer


# Create your views here.


class UserView(generics.GenericAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
