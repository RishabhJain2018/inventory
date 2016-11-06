from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import (
	UserSerializer,
	CategorySerializer,
	StatSerializer,
	ProductSerializer,
	)
from .models import Category, Stat, Product


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def get_queryset(self):
		queryset = Category.objects.filter(status=1)
		return queryset

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		if Stat.objects.exists():
			s = Stat.objects.get()
			s.category_count +=1
			s.save()
		else:
			Stat.objects.create(category_count=1)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		s=Stat.objects.get()
		s.category_count -= 1
		if s.category_count < 1:
			s.category_count = 0
		s.save()
		return Response(status=status.HTTP_204_NO_CONTENT)


class StatViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Stat.objects.all()
	serializer_class = StatSerializer


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get_queryset(self):
		queryset = Product.objects.all()

		category_id = self.kwargs.get('category_pk', None)
		product_id = self.kwargs.get('pk', None)

		if category_id:
			Category = Category.objects.get(id=category_id)
			queryset = queryset.filter(category=category)

		if product_id:
			queryset = queryset.filter(id=product_id)

		return queryset

