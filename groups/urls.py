from django.urls import path
from . import views

urlpatterns = [
    path("groups/", views.GroupView.as_view()),
    path("groups/<pk>/", views.GroupDetailView.as_view()),
]