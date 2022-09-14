from django.urls import path
from . import views

urlpatterns = [
    path("posts/<str:group_id>/", views.PostView.as_view(), name="groups"),
    path("posts/detail/<pk>/", views.PostDetailView.as_view(), name="groups-detail"),
]