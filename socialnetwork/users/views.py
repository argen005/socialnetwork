from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
