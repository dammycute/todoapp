from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import *
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
# import requests

# Create your views here.


class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class AuthUserApiView(GenericAPIView):
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request):
#         user = request.user
#         serializer = RegisterSerializer(user)

#         response.Response({"user": serializer.data})
    


# class LoginApiView(GenericAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = LoginSerializer
#     def post(self, request):
#         email = request.data.get('email', None)
#         password = request.data.get('password', None)
        
#         user = authenticate(username=email, password=password)

#         if user:
#             serializer = self.serializer_class(user)
#             return response.Response(serializer.data, status=status.HTTP_200_OK)
#         return response.Response({"message": "Invalid Credential, try again"}, status=status.HTTP_401_UNAUTHORIZED)