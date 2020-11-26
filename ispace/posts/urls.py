from django.urls import path

from .views import PostCreateView, PostDeleteView, PostDetailView, PostEditView

app_name = "posts"
urlpatterns = [
    path("create/", PostCreateView.as_view(), name="create"),
    path("<slug:slug>/", PostDetailView.as_view(), name="detail"),
    path("<slug:slug>/edit/", PostEditView.as_view(), name="edit"),
    path("<slug:slug>/delete/", PostDeleteView.as_view(), name="delete"),
]
