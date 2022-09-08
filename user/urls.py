from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("users/login", obtain_auth_token),
    path("users", views.UserView.as_view()),
    path("users/<pk>/",views.UserDetailView.as_view()),
]
