"""Test forms for form helpers.
"""

from django import forms

from pebble_helpers.forms.mixins import FormLabelSuffixMixin


class LabelSuffixTestForm(FormLabelSuffixMixin, forms.Form):
    """A form to test the default label_suffix override
    """
    test_field = forms.CharField()


class LabelSuffixInClassTestForm(LabelSuffixTestForm):
    """A form to test that label_suffix can be set on a class
    """
    label_suffix = '>'
