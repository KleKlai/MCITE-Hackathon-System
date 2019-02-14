from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer, RegisterSerializer
from .managers import UserManager
from rest_framework.exceptions import ValidationError
from django.contrib.auth.views import PasswordResetView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class Login(APIView):
    """login
    """

    serializer_class = LoginSerializer # serializer class for turning data into JSON serializable data 
    permission_classes = (AllowAny,) # allow any authenticated/unauthenticated users to view the API

    def post(self,*args,**kwargs): # post request will always be used when passing data to the API
        serializer = self.serializer_class( # validate data below
            data=self.request.data, request=self.request) # self.request.data (this are all the data passed from the front-end (Angular 7 services) ) 

        serializer.is_valid(raise_exception=True) # check if data are all valid, this will return True, or else it will return a exception error
        token, _ = Token.objects.get_or_create(user=serializer.user) # create a token for the user, for user authentication in Angular

        return Response({ # return a token for user authentication in Angular
            'token': token.key,
        }, status=200, headers={'Authorization': 'Token {}'.format(token.key)}) 


class Register(APIView):
    """register
    """

    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(
            data=self.request.data)
        
        serializer.is_valid(raise_exception=True) # check if the data are all valid, this will return True, or else it will return a exception error
    
        user = serializer.save() # if data are valid, it will create a new user, hence if the data are invalid, it means the user acount already existed or has incorrect format typed in the form fields
        user.set_password(serializer.data['password'])  # sets the password for the user
        user.save() # finally save the user model changes after setting a password

        token, _ = Token.objects.get_or_create(user=user) # create a token for the user
        
        return Response({ # return a token for user authentication in Angular
            'token': token.key,
        }, status=200, headers={'Authorization': 'Token {}'.format(token.key)})