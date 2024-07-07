from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.ListTodosAPIView.as_view(), name='list_todos_only_id'),
    path('todos/titles/', views.ListTodosWithTitleAPIView.as_view(), name='list_todos_with_titles'),
    path('todos/pending/', views.ListPendingTodosAPIView.as_view(), name='list_pending_todos'),
    path('todos/completed/', views.ListCompletedTodosAPIView.as_view(), name='list_completed_todos'),
    path('todos/user_ids/', views.ListTodosWithUserIdAPIView.as_view(), name='list_todos_with_user_id'),
    path('todos/completed_user_ids/', views.ListCompletedTodosWithUserIdAPIView.as_view(), name='list_completed_todos_with_user_id'),
    path('todos/pending_user_ids/', views.ListPendingTodosWithUserIdAPIView.as_view(), name='list_pending_todos_with_user_id'),
]
