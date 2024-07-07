from django.shortcuts import render
from django.http import JsonResponse
from ToDoPendings.models import Todo
from rest_framework import serializers


# serializers.py

# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id','title','description','status','user_id','created_at','updated_at','user']
#         read_only_fields = ['created_at','updated_at','user_id']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'user_id', 'created_at', 'updated_at', 'user']
        read_only_fields = ['created_at', 'updated_at', 'user_id']

class ListTodosWithTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id','title']

class ListPendingTodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']

class ListCompletedTodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']

class ListTodosWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user_id']

class ListCompletedTodosWithUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user_id']

class ListPendingTodosWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user_id']