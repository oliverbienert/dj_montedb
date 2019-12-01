from django.forms import ModelForm

from .models import Child


class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ["first_name",
                  "last_name",
                  "birth_date",
                  "birth_place",
                  "care_time",
                  "kita"]
