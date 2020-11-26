from django.urls import path

from .views import (
    HubCreateView,
    HubDeleteView,
    HubDetailView,
    HubEditView,
    HubJoinView,
    HubLeaveView,
)

app_name = "hubs"
urlpatterns = [
    path("create/", HubCreateView.as_view(), name="create"),
    path("<slug:slug>/", HubDetailView.as_view(), name="detail"),
    path("<slug:slug>/join/", HubJoinView.as_view(), name="join"),
    path("<slug:slug>/leave/", HubLeaveView.as_view(), name="leave"),
    path("<slug:slug>/edit/", HubEditView.as_view(), name="edit"),
    path("<slug:slug>/delete/", HubDeleteView.as_view(), name="delete"),
]
