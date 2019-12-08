import django_tables2 as tables

from .models import Child


class ChildTable(tables.Table):
    class Meta:
        model = Child
        template_name = "django_tables2/bootstrap.html"
        fields = ("first_name", "last_name")
