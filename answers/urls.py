from django.urls import path
from . import views

urlpatterns = [
    path("groups/<int:group_id>/posts/answers/<int:comment_id>", views.AnswerView.as_view()),
    path("answers/<pk>/", views.AnswerDetailView.as_view()),
]