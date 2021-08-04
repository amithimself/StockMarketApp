from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Stock
from .serializer import StockSerializer, StockDetailsSerializer


# Create your views here.


class StockView(generics.GenericAPIView, mixins.ListModelMixin,
                mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):
    serializer_class = StockDetailsSerializer
    queryset = Stock.objects.all()
    lookup_field = 'stock_name'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, stock_name=None):
        if stock_name:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, stock_name=None):
        return self.update(request, stock_name)

    def delete(self, request, stock_name=None):
        return self.destroy(request, stock_name)


class StockListView(generics.GenericAPIView, mixins.ListModelMixin
                    ):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
