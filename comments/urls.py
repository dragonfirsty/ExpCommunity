from django.urls import path
from . import views

urlpatterns = [
    path("comments/<str:post_id>/", views.CommentView.as_view()),
    path("comments/detail/<pk>/", views.CommentDetailView.as_view()),
]