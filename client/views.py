import typing

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.forms import ClientForms
from client.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра сущностей"""
    model = Client
    template_name = 'client/client_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class ClientDetailView(DetailView):
    """Контроллер для просмотра сущности"""
    model = Client
    template_name = 'client/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания сущности"""
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('client:client_list')

    def form_valid(self, form: typing.Any) -> typing.Any:
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения сущности"""
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('client:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404("Доступ запрещен")
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления сущности"""
    model = Client
    success_url = reverse_lazy('client:client_list')
