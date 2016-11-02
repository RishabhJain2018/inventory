from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import (
	UserSerializer,
	CategorySerializer,
	)
from .models import Category


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def get_queryset(self):
		queryset = Category.objects.all()
		return queryset

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)

