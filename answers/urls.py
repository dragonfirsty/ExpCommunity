from django.urls import path
from . import views

urlpatterns = [
    path("answers/", views.AnswerView.as_view()),
    path("answers/<pk>/", views.AnswerDetailView.as_view()),
]