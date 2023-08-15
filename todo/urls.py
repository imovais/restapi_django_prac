from django.urls import path

from . import views

urlpatterns = [
    #path("", views.home, name="index"),
    path("entries/", views.entries, name="entries"),
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/", views.UpdateTodoAPIView.as_view(),name="todo_update"),
]