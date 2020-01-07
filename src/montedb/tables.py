from django_tables2 import tables, TemplateColumn

from .models import Child


class ChildTable(tables.Table):
    class Meta:
        model = Child
        fields = ("first_name", "last_name", "birth_date", "birth_place", "care_time", "kita")

        buttons = TemplateColumn(template_name="montedb/table_buttons.html", orderable=False, verbose_name="")
