from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView
from .models import Adult, Child
from .forms import AdultForm, ChildForm
from .tables import AdultTable, ChildTable
from django.urls import reverse_lazy

child_fields = ["first_name", "last_name",
                "birth_date",
                "birth_place",
                "care_time",
                "kita"]

adult_fields = ["first_name",
                "last_name",
                "birth_date",
                "iban"]


class ChildrenView(SingleTableView):
    template_name = "montedb/child_list.html"
    table_class = ChildTable
    model = Child


class ChildCreate(CreateView):
    model = Child
    form_class = ChildForm
    title = "Kind hinzufügen"
    template_name = "montedb/child_form.html"
    success_url = reverse_lazy('child-list')


class ChildUpdate(UpdateView):
    model = Child
    form_class = ChildForm
    title = "Kind bearbeiten"
    template_name = "montedb/child_form.html"
    success_url = reverse_lazy('child-list')


class ChildDelete(DeleteView):
    model = Child
    success_url = reverse_lazy('child-list')


class AdultsView(SingleTableView):
    template_name = "montedb/adult_list.html"
    table_class = AdultTable
    model = Adult


class AdultCreate(CreateView):
    model = Adult
    form_class = AdultForm
    title = "Erwachsenen hinzufügen"
    template_name = "montedb/adult_form.html"
    success_url = reverse_lazy('adult-list')


class AdultUpdate(UpdateView):
    model = Adult
    form_class = AdultForm
    title = "Erwachsenen bearbeiten"
    template_name = "montedb/adult_form.html"
    success_url = reverse_lazy('adult-list')


class AdultDelete(DeleteView):
    model = Adult
    success_url = reverse_lazy('adult-list')