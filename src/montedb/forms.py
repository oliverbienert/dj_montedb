import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, MultiWidgetField
from django.forms import ModelForm, SelectDateWidget

from .models import Child


class ChildForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        year = datetime.datetime.today().year
        self.fields["birth_date"].widget = SelectDateWidget(years=list(range(year, year -100, -1)))

        self.helper.layout = Layout(
            Field("first_name", placeholder="Vorname", autofocus=""),
            Field("last_name", placeholder="Nachname"),
            MultiWidgetField('birth_date', placeholder='Geburtsdatum', css_class='selectdatewidget', attrs=({'style': 'display: inline-block;'})),
            Field("birth_place", placeholder="Geburtsort"),
            Field("care_time", placeholder="Betreuungszeit"),
            Field("kita", placeholder="Kita"),
            Submit("add", "Hinzufügen", css_class="btn btn-lg btn-primary btn-block"),
        )

    class Meta:
        model = Child
        fields = "__all__"
