from django.urls import path
from . import views

urlpatterns = [
    path("answers/<str:comment_id>/", views.AnswerView.as_view()),
    path("answers/detail/<pk>/", views.AnswerDetailView.as_view()),
]