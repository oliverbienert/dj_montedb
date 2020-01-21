from django_tables2 import tables, TemplateColumn

from .models import Adult, Child

attrs = {
    'data-toggle': 'table',
    'data-classes': 'table table-striped table-hover',
    'data-mobile-responsive': 'true'
}


class ChildTable(tables.Table):
    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'birth_date', 'birth_place', 'care_time', 'kita')
        attrs = attrs

    buttons = TemplateColumn(template_name='montedb/child_table_buttons.html', orderable=False, verbose_name="")


class AdultTable(tables.Table):
    class Meta:
        model = Adult
        fields = {'first_name', 'last_name', 'birth_date', 'iban', 'partner'}
        sequence = ('first_name', 'last_name', 'birth_date', 'iban', '...')
        attrs = attrs

    buttons = TemplateColumn(template_name='montedb/adult_table_buttons.html', orderable=False, verbose_name="")
