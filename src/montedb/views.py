from django.views.generic import ListView
from .models import Child
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class ChildrenView(ListView):
    template_name = "child_list.html"
    model = Child

