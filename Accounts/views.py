from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from Accounts.renderers import UserRenderer
from .models import User
from .utils import Util
from Accounts.serializers import (

    UserLoginSerializer,
    UserPasswordChangeSerializer,
    PasswordResetSerializer,
    UserProfileSerializer,
    UserPasswordResetSerializer,
    UserProfileSerializer,
    UserSerializer,
    ProfileSerializer
)

# Create your views here.


#....................token generation.............................


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# registering user


# class UserRegistrationView(APIView):
#     renderer_classes = [UserRenderer]

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save(is_active = False)
#             self.send_verification_email(request, user)
#             token = get_tokens_for_user(user)
#             return Response(
#                 {"token": token, "msg": "registratio succesful"},
#                 status=status.HTTP_201_CREATED,
#             )

#         return Response(serializer.errors, status=status)
    
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # extracting user id from the registered user
            uid = user.id

            # email sending after the user is registered and save
            data = {
                "subject":"Django Email",
                "body" : user.name
                +""
                + "you have been succesfully registered in our site ",
                "to_email": user.email,
            }
            Util.send_email(data)

            # self.send_verification_email(request, user)
            token = get_tokens_for_user(user)
            return Response(
                {
                  "uid": uid,
                  "token": token,
                  "msg": "registratio succesful"
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    






## views for User Profile
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,format=None):
        serializer = UserProfileSerializer(request.user)
        # serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)



# User Login
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"token": token, "msg": "login succesful"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["email or password is not valid"]
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserPasswordChangeView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserPasswordChangeSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"mag": "password change succesfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serialzer = PasswordResetSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            return Response(
                {"mag": "password reset link sent"}, status=status.HTTP_200_OK
            )
        # return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
   
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"mag": "password reset succesfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#  ogin on the Role base.
    
    class UserLoginView(APIView):
        def post(self, request, format=None):
            email = request.get(email = email)
            password = request.get(password = password)
            user = authenticate(email = email,password = password)
            if user:
                if user.role == 'student':
                    return Response({"mag":"login succesful for student"},status=status.HTTP_200_OK)
                elif user.role == 'teacher':
                    return Response({"msg":"login succesful for teacher"},status=status.HTTP_200_OK)
                else:
                    return Response({"msg":"user role is unknown"},status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"msg":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)    