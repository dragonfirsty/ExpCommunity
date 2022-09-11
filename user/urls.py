from django.urls import path
from . import views

urlpatterns = [
    path("users/login/", views.UserLogin.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<pk>/",views.UserDetailView.as_view()),
]

