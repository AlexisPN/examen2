from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ToDoPendings.models import Todo
from .serializers import (
    TodoSerializer,
    ListTodosWithTitleSerializer,
    ListPendingTodosSerializer,
    ListCompletedTodosSerializer,
    ListTodosWithUserSerializer,
    ListCompletedTodosWithUserIdSerializer,
    ListPendingTodosWithUserSerializer,
)

class ListTodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class ListTodosWithTitleAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = ListTodosWithTitleSerializer(todos, many=True)
        return Response(serializer.data)

class ListPendingTodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(status='PENDING')
        serializer = ListPendingTodosSerializer(todos, many=True)
        return Response(serializer.data)

class ListCompletedTodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(status='COMPLETED')
        serializer = ListCompletedTodosSerializer(todos, many=True)
        return Response(serializer.data)

class ListTodosWithUserIdAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = ListTodosWithUserSerializer(todos, many=True)
        return Response(serializer.data)

class ListCompletedTodosWithUserIdAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(status='COMPLETED')
        serializer = ListCompletedTodosWithUserIdSerializer(todos, many=True)
        return Response(serializer.data)

class ListPendingTodosWithUserIdAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(status='PENDING')
        serializer = ListPendingTodosWithUserSerializer(todos, many=True)
        return Response(serializer.data)
