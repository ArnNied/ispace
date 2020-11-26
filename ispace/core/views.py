from django.views.generic import ListView
from hubs.models import Hub
from posts.models import Post

from ispace.users.models import User


# Create your views here.
class IndexListView(ListView):
    """View for index page."""

    model = Post
    context_object_name = "posts_list"
    ordering = "-date_posted"
    template_name = "core/index.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset


class SearchView(ListView):
    """View for search page."""

    model = Post
    context_object_name = "posts_list"
    template_name = "core/search.html"

    def get_queryset(self):
        query = self.request.GET.get("query", "")

        # Main query for search page.
        queryset = super().get_queryset()
        queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("query", "")

        # Additional data (hubs and users) on the search page.
        context = super().get_context_data(**kwargs)
        context["hubs_list"] = Hub.objects.filter(name__istartswith=query)[:5]
        context["users_list"] = User.objects.filter(username__istartswith=query)[:5]

        return context
