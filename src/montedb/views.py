from django_tables2 import SingleTableView
from .models import Adult, Child
from .tables import AdultTable, ChildTable


class ChildrenView(SingleTableView):
    template_name = "montedb/child_list.html"
    table_class = ChildTable
    model = Child

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ChildrenView, self).get_context_data(**kwargs)
        context['children'] = 'active'
        return context


class AdultsView(SingleTableView):
    template_name = "montedb/adult_list.html"
    table_class = AdultTable
    model = Adult

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AdultsView, self).get_context_data(**kwargs)
        context['adults'] = 'active'
        return context
