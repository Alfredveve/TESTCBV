from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Service
from django.urls import reverse_lazy


class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'



class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/service_detail.html'


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'service/service_form.html'
    fields = ['title', 'description', 'price', 'image']


class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'service/service_form.html'
    fields = ['title', 'description', 'price', 'image']


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
