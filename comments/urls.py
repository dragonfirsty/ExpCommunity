from django.urls import path
from . import views

urlpatterns = [
    path("comments/", views.CommentView.as_view()),
    path("comments/<pk>/", views.CommentDetailView.as_view()),
]