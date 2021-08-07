from rest_framework import serializers
from category.models import Category,TodoList


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields='__all__'
