from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .helper import *


# Create your views here.

class MyfriendsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            profile = UserProfile.objects.get(user=user)
            profile_serializer = UserProfileSerializer(profile)

            friends_profiles = UserProfile.objects.filter(id__in=profile.friends.values_list('id', flat=True))
            friends_serializer = UserProfileSerializer(friends_profiles, many=True)

            response_data = {
                "user": UserSerializer(user).data,  # Serialize the user object
                "friends": friends_serializer.data  # Serialize the friends' profiles
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdateUserProfileView(APIView):

    can_patch = ['current_state', 'img', 'XP', 'lvl','friends']

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        users = get_user_model().objects.filter(is_superuser=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        data = request.data
        user = request.user

        if data.get('userID'):
            return Response({"error": "userID cannot change"}, status=status.HTTP_400_BAD_REQUEST)
        if data.get('friends'):
            return Response({"error": "friend logic is pending"}, status=status.HTTP_400_BAD_REQUEST)


        profile_data = {key: data[key] for key in self.can_patch if key in data}
        if not profile_data:
            return Response({"error":"No field match"},status=status.HTTP_204_NO_CONTENT)

        profile = UserProfile.objects.get(user=user)
        profile_serializer = UserProfileSerializer(profile, data=profile_data, partial=True)

        if profile_serializer.is_valid():
            profile_serializer.save()
            print(profile_serializer.data)
            response_data = {key: profile_serializer.data[key] for key in profile_serializer.data if key in data}
            return Response(response_data, status=status.HTTP_200_OK)
        
        print(profile_serializer.data)
        print(profile_serializer.is_valid())
        return Response({"error": profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serail = RegisterSerializer(data=data)

        if not serail.is_valid():
            return Response({"error": serail.errors}, status=status.HTTP_400_BAD_REQUEST)

        serail.save()
        response_data = serail.data.copy()  # Make a copy of the serialized data
        response_data.pop('password', None)  # Remove the password field if it exists
        return Response({"status":"Success","data": response_data}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        serail = LoginSerializer(data=data)

        if not serail.is_valid():
            return Response({"error": serail.errors}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serail.data['username'], password=serail.data['password'])

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token, _ = Token.objects.get_or_create(user=user)
        except Exception as e:
            print(e)
            return Response({"error": e}, status=status.HTTP_409_CONFLICT)
        
        try:
            user_profile = UserProfile.objects.get(user = user)
            response_data = get_user_extra_fields(user,user_profile)
        except Exception as e:
            return Response({"status":"fail to load user_extra fields data", "error":str(e)})
        return Response({"data": response_data, 'token': str(token)}, status=status.HTTP_202_ACCEPTED)
