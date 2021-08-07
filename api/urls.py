from django.urls import path
from .views import apiOverview, List_Categories_APIView ,List_and_Create_Todos_APIView, Delete_APIView

urlpatterns = [
    path('overview/', apiOverview.as_view()),
    path('list_category/', List_Categories_APIView.as_view()),
    path('list_create_todo/', List_and_Create_Todos_APIView.as_view()),
    path('delete_todo/<int:id>/', Delete_APIView.as_view()),
]
