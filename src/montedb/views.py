from django.views.generic import ListView
from .models import Child
from .forms import ChildForm, ChildDeleteForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

child_fields = ["first_name", "last_name",
                "birth_date",
                "birth_place",
                "care_time",
                "kita"]


class ChildrenView(ListView):
    template_name = "montedb/child_list.html"
    model = Child


class ChildCreate(CreateView):
    model = Child
    form_class = ChildForm
    template_name = "montedb/child_form.html"


class ChildUpdate(UpdateView):
    model = Child
    form_class = ChildForm
    template_name = "montedb/child_form.html"


class ChildDelete(DeleteView):
    model = Child
    form_class = ChildDeleteForm
    success_url = reverse_lazy('child-list')
