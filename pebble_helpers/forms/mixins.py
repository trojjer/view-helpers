"""Mixins to help with forms.
"""

class FormLabelSuffixMixin(object):
    """
    Overrides the default label_suffix,
    which must be passed as a kwarg on init.
    This also allows setting on a form class.
    """
    def __init__(self, *args, **kwargs):
        suffix = getattr(self, 'label_suffix', '')
        kwargs.setdefault('label_suffix', suffix)
        super(FormLabelSuffixMixin, self).__init__(*args, **kwargs)
