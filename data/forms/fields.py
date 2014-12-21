from django import forms
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


__all__ = (
    'RangeInput', 'InlineCheckboxSelectMultiple',
)


class RangeInput(forms.TextInput):
    input_type = 'range'


class InlineChoiceInput(forms.widgets.ChoiceInput):
    def render(self, name=None, value=None, attrs=None, choices=()):
        if self.id_for_label:
            label_for = format_html(' for="{0}"', self.id_for_label)
        else:
            label_for = ''
        return format_html('<label{0} class="{1}-inline">{2} {3}</label>', label_for, self.input_type, self.tag(), self.choice_label)


class InlineCheckboxChoiceInput(InlineChoiceInput):
    input_type = 'checkbox'

    def __init__(self, *args, **kwargs):
        super(InlineCheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.value = set(force_text(v) for v in self.value)

    def is_checked(self):
        return self.choice_value in self.value


class InlineChoiceFieldRenderer(forms.widgets.ChoiceFieldRenderer):
    def render(self):
        """
        Outputs a <ul> for this set of choice fields.
        If an id was given to the field, it is applied to the <ul> (each
        item in the list will get an id of `$id_$i`).
        """
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<div class="inline-choice" id="{0}">', id_) if id_ else '<div class="inline-choice">'
        output = [start_tag]
        for i, choice in enumerate(self.choices):
            choice_value, choice_label = choice
            if isinstance(choice_label, (tuple, list)):
                attrs_plus = self.attrs.copy()
                if id_:
                    attrs_plus['id'] += '_{0}'.format(i)
                sub_ul_renderer = InlineChoiceFieldRenderer(name=self.name,
                                                      value=self.value,
                                                      attrs=attrs_plus,
                                                      choices=choice_label)
                sub_ul_renderer.choice_input_class = self.choice_input_class
                output.append(format_html('{0}{1}', choice_value,
                                          sub_ul_renderer.render()))
            else:
                w = self.choice_input_class(self.name, self.value,
                                            self.attrs.copy(), choice, i)
                output.append(format_html('{0}', force_text(w)))
        output.append('</div>')
        return mark_safe('\n'.join(output))

class InlineCheckboxFieldRenderer(InlineChoiceFieldRenderer):
    choice_input_class = InlineCheckboxChoiceInput


class InlineCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    renderer = InlineCheckboxFieldRenderer