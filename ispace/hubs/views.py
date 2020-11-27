from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    RedirectView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin

from ispace.users.models import User

from .models import Hub


# Create your views here.
class HubDetailView(DetailView):
    """View for detail page of a Hub."""

    model = Hub
    context_object_name = "hub"
    ordering = "-date_posted"
    paginate_by = 10
    template_name = "hubs/detail.html"


class HubCreateView(LoginRequiredMixin, CreateView):
    """View for creating a Hub."""

    model = Hub
    template_name = "hubs/create.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Form allowed data initialization to prevent client-side modification.
        context["form"].fields["owner"].initial = self.request.user.id
        context["form"].fields["owner"].queryset = User.objects.filter(
            pk=self.request.user.id
        )

        return context


class HubEditView(LoginRequiredMixin, UpdateView):
    """View for editing a Hub."""

    model = Hub
    template_name = "hubs/edit.html"
    fields = ["name", "description"]

    def get_object(self, queryset=None):
        obj = super().get_object()

        # Ensure object is owned by current user (request.user).
        if obj.owner != self.request.user:
            raise PermissionDenied

        return obj


class HubDeleteView(LoginRequiredMixin, DeleteView):
    model = Hub
    context_object_name = "hub"
    template_name = "hubs/delete_confirmation.html"

    def get_object(self, queryset=None):
        obj = super().get_object()

        # ensure object is owned by current user (request.user).
        if obj.owner != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse("core:index")


class HubLeaveJoin(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    """Parent class for HubJoinView and HubLeaveView."""

    model = Hub
    permanent = True
    pattern_name = "hubs:detail"


class HubJoinView(HubLeaveJoin):
    """View for joining a Hub."""

    def post(self, request, *args, **kwargs):
        hub = self.get_object()

        # Prevent owner from joining their own Hub.
        if hub.owner == self.request.user:
            raise PermissionDenied

        hub.member.add(self.request.user)

        return super().post(request, *args, **kwargs)


class HubLeaveView(HubLeaveJoin):
    """View for leaving a Hub."""

    def post(self, request, *args, **kwargs):
        hub = self.get_object()

        # Prevent owner from leaving their own Hub.
        if hub.owner == self.request.user:
            raise PermissionDenied

        hub.member.remove(self.request.user)

        return super().post(request, *args, **kwargs)
