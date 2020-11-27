from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from ispace.users.models import User

from .models import Post


# Create your views here.
class PostDetailView(DetailView):
    """View for detail page of a Hub."""

    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for creating a Hub."""

    model = Post
    template_name = "posts/create.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Form allowed data initialization to prevent client-side modification.
        form = context["form"]

        form.fields["user"].initial = self.request.user.id
        form.fields["user"].queryset = User.objects.filter(pk=self.request.user.id)
        form.fields["hub"].queryset = (
            self.request.user.joined_hub.all() | self.request.user.owned_hub.all()
        )

        return context


class PostEditView(LoginRequiredMixin, UpdateView):
    """View for editing a hub."""

    model = Post
    template_name = "posts/edit.html"
    fields = ["title", "body"]

    def get_object(self, queryset=None):
        obj = super().get_object()

        # Ensure object is owned by current user (request.user).
        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """View for deleting a hub."""

    model = Post
    template_name = "posts/delete_confirmation.html"

    def get_object(self, queryset=None):
        obj = super().get_object()

        # Ensure object is owned by current user (request.user).
        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse("core:index")
