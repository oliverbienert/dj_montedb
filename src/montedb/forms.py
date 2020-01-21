import datetime

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, MultiWidgetField, Button, Fieldset, ButtonHolder, HTML
from django.db.models import Q
from django.forms import ModelForm, SelectDateWidget, ModelChoiceField

from .models import Adult, Child

submit_css_class = "btn btn-lg btn-primary btn-block"


class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        year = datetime.datetime.today().year
        self.fields["birth_date"].widget = SelectDateWidget(years=list(range(year, year -100, -1)))


class ChildForm(PersonForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Fieldset(
                'Personal data',
                Field("first_name", placeholder="First name", autofocus=""),
                Field("last_name", placeholder="Last name"),
                MultiWidgetField('birth_date', placeholder='Birth date', css_class='selectdatewidget', attrs=({'style': 'display: inline-block;'})),
                Field("birth_place", placeholder="Birth place"),
                Field("care_time", placeholder="Care time"),
                Field("kita", placeholder="Nursery")
            ),
            FormActions(
                Submit("add", "{{ view.title }}"),
                HTML('<a href="{{ view.success_url }}" class="btn btn-secondary">Cancel</a>')
            )
        )

    class Meta:
        model = Child
        fields = "__all__"


class AdultForm(PersonForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Fieldset(
                'Personal data',
                Field("first_name", placeholder="First name", autofocus=""),
                Field("last_name", placeholder="Last name"),
                MultiWidgetField('birth_date', placeholder='Birth date', css_class='selectdatewidget', attrs=({'style': 'display: inline-block;'})),
                Field("iban", placeholder="IBAN"),
                Field("partner")
            ),
            FormActions(
                Submit("add", "{{ view.title }}"),
                HTML('<a href="{{ view.success_url }}" class="btn btn-secondary">Cancel</a>')
            )
        )
        self.fields['partner'].queryset = Adult.objects\
            .filter(Q(partner=None) | Q(partner=self.instance))\
            .exclude(pk=self.instance.pk)

    class Meta:
        model = Adult
        fields = "__all__"

