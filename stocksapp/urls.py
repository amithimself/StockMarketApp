from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from allauth.account.views import confirm_email
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import StockListView, StockView


urlpatterns = [

    path('api/stock/<str:stock_name>', StockView.as_view()),
    path('api/stock/', StockListView.as_view()),

]
