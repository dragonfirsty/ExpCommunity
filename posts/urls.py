from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:group_id>/", views.PostView.as_view()),
    path("posts/<pk>/", views.PostDetailView.as_view()),
]