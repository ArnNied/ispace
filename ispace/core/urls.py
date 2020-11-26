from django.urls import path

from .views import IndexListView, SearchView

app_name = "core"
urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("search/", SearchView.as_view(), name="search"),
    # path("latest/", IndexListView.as_view(), name="latest"),
    # path("popular/", IndexListView.as_view(), name="popular"),
    # path("joined/", IndexListView.as_view(), name="joined_hub"),
]
