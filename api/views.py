from django.shortcuts import render

from .serializers import CategorySerializer, TodoListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from category.models import Category, TodoList
# Create your views here.

#list available urls
class apiOverview(APIView):

	def get(self, request):
          api_urls = {
               'List Categories': 'api/list_category/',
               # 'List and Add Tasks': 'api/list_create_todo/',
               'List and Add Tasks': 'http://127.0.0.1:8000/api/list_create_todo/',
               'Delete Task': 'api/delete_todo/<int:id>/',
               }
               
          return Response(api_urls)

# get categories views
class List_Categories_APIView(generics.GenericAPIView, mixins.ListModelMixin):
	serializer_class = CategorySerializer
	queryset = Category.objects.all().order_by('-id')

	def get(self, request):
		return self.list(request)

# get and create todos views
class List_and_Create_Todos_APIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
	serializer_class = TodoListSerializer
	queryset = TodoList.objects.all().order_by('-id')

	def get(self, request):
		return self.list(request)

	def post(self, request):
		return self.create(request)

# delete todo
class Delete_APIView(generics.GenericAPIView, mixins.ListModelMixin,
						 mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	serializer_class = TodoListSerializer
	queryset = TodoList.objects.all().order_by('-id')

	lookup_field= 'id'

	def get(self, request, id=None):
		
		if id:
			return self.retrieve(request)
		
		else:
			return self.list(request)
	
	def delete(self, request, id):
		return self.destroy(request, id)
