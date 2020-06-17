from django_tables2 import tables, TemplateColumn

from .models import Adult, Child

attrs = {
    'data-toggle': 'table',
    'data-classes': 'table table-striped table-hover table-sm',
    'data-mobile-responsive': 'true'
}


class ChildTable(tables.Table):
    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'birth_date', 'birth_place', 'care_time', 'kita')
        attrs = attrs


class AdultTable(tables.Table):
    class Meta:
        model = Adult
        fields = {'first_name', 'last_name', 'birth_date', 'iban', 'partner'}
        sequence = ('first_name', 'last_name', 'birth_date', 'iban', '...')
        attrs = attrs

    buttons = TemplateColumn(template_name="montedb/parent_contribution_button.html", orderable=False, verbose_name="")
