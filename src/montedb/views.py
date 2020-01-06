from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView
from .models import Child
from .forms import ChildForm
from .tables import ChildTable
from django.urls import reverse_lazy

child_fields = ["first_name", "last_name",
                "birth_date",
                "birth_place",
                "care_time",
                "kita"]


class ChildrenView(SingleTableView):
    template_name = "montedb/child_list.html"
    table_class = ChildTable
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
    success_url = reverse_lazy('child-list')
