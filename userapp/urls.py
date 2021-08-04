from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from allauth.account.views import confirm_email
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserView


urlpatterns = [
    url(r'^api/user/', include('rest_auth.urls')),
    url(r'^api/user/register/', include('rest_auth.registration.urls')),
    url(r'^api/account/', include('allauth.urls')),
    path('api/user/<int:id>/', UserView.as_view()),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),

]
