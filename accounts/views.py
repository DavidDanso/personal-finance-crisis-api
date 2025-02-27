from rest_framework import generics
from .models import UserProfile
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)