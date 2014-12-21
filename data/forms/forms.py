from django import forms
from .fields import *


__all__ = (
    'DataForm',
)


def get_field_for_datum(datum_type):
    return {
        'long_text': forms.CharField(widget=forms.Textarea),
        'short_text': forms.CharField(),
        'choice': forms.ChoiceField(),
        'multi_choice': forms.MultipleChoiceField(widget=InlineCheckboxSelectMultiple()),
        'numeric': forms.IntegerField(),
        'range': forms.IntegerField(widget=RangeInput()),
    }[datum_type]


class DataForm(forms.Form):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)

        # get all data-points for this user
        for datum in user.datum_set.filter(active=True).all():
            field = get_field_for_datum(datum.datum_type)
            field.required = False
            field.label = datum.prompt
            field.choices = [(c.id, c.value) for c in datum.choice_set.all()]

            if datum.has_max_and_min():
                field.widget.attrs['step'] = 1
                field.widget.attrs['max'] = datum.max_value
                field.widget.attrs['min'] = datum.min_value

            self.fields['datum_{}'.format(datum.id)] = field


