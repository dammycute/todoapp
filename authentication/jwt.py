# from rest_framework.authentication import get_authorization_header, BaseAuthentication
# from rest_framework import exceptions
# from django.conf import settings
# import jwt
# from authentication.models import User


# class JWTAuthentication(BaseAuthentication):

#     def authenticate(self, request):

#         auth_header = get_authorization_header(request)
#         auth_data = auth_header.decode('utf-8')

#         auth_token = auth_data.split(" ")

#         if len(auth_token) != 2:
#             raise exceptions.AuthenticationFailed('Token not Valid')
        
#         token = auth_token[1]

#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

#         username = payload['username']

#         user = User.objects.get(username=username)

#         return (user, token)

#         try:
#             return super().authenticate(request)
        
#         except jwt.ExpiredSignatureError as e:
#             raise exceptions.AuthenticationFailed(
#                 "Token is expired, login again"
#             )

#         except jwt.DecodeError as e:
#             raise exceptions.AuthenticationFailed(
#                 "Token is invalid"
#             )

#         except User.DoesNotExist as no_user:
#          raise exceptions.AuthenticationFailed(
#             "User does not exist"
#         )

#         return super().authenticate(request)