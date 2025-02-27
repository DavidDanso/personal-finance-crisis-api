from rest_framework import generics
from .models import UserProfile
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer

#
class UserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


