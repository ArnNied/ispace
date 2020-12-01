from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from posts.models import Post

User = get_user_model()


class UserDetailView(LoginRequiredMixin, ListView):

    model = Post
    context_object_name = "posts"
    ordering = "-date_posted"
    paginate_by = 10
    template_name = "users/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user
        context["user"] = get_object_or_404(User, username=self.kwargs["username"])

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the user's Post item
        queryset = queryset.filter(user__username=self.kwargs["username"])

        return queryset


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["username"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=None):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
