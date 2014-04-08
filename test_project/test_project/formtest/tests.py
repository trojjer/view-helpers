"""Test the Form-based view and form mixins.
"""
from unittest import TestCase as UnitTestCase

from test_project.formtest.views import (FailureUrlView, FailureUrlArgView,
        FailureUrlKwargView, FailureUrlArgKwargView, SuccessUrlView,
        SuccessUrlArgView, SuccessUrlKwargView, SuccessUrlArgKwargView,
        NoUrlView)

from test_project.formtest.forms import (LabelSuffixTestForm,
    LabelSuffixInClassTestForm)


class RedirectReverseTestCase(UnitTestCase):
    """Test the RedirectReverseTestCase.
    """
    def test_success_url_plain(self):
        """Test the success url is reversed.
        """
        v = SuccessUrlView()
        self.assertEqual(v.get_success_url(), '/success/plain/')

    def test_failure_url_plain(self):
        """Test the failure url is reversed.
        """
        v = FailureUrlView()
        self.assertEqual(v.get_failure_url(), '/failure/plain/')

    def test_success_url_arg(self):
        """Test the success url is reversed with the given arg.
        """
        v = SuccessUrlArgView()
        self.assertEqual(v.get_success_url(), '/success/arg/0/')

    def test_failure_url_arg(self):
        """Test the failure url is reversed with the given arg.
        """
        v = FailureUrlArgView()
        self.assertEqual(v.get_failure_url(), '/failure/arg/0/')

    def test_success_url_kwarg(self):
        """Test the success url is reversed with the given kwarg.
        """
        v = SuccessUrlKwargView()
        self.assertEqual(v.get_success_url(), '/success/kwarg/0/')

    def test_failure_url_kwarg(self):
        """Test the failure url is reversed with the given kwarg.
        """
        v = FailureUrlKwargView()
        self.assertEqual(v.get_failure_url(), '/failure/kwarg/0/')

    def test_success_argkwarg(self):
        """We get a ValueError on defining both args and kwargs.
        """
        v = SuccessUrlArgKwargView()

        self.assertRaises(ValueError, v.get_success_url)

    def test_failure_argkwarg(self):
        """We get a ValueError on defining both args and kwargs.
        """
        v = FailureUrlArgKwargView()

        self.assertRaises(ValueError, v.get_failure_url)

    def test_no_success_url(self):
        """We get an error when no success_url is defined.
        """
        v = NoUrlView()
        self.assertRaises(NotImplementedError, v.get_success_url)

    def test_no_failure_url(self):
        """We get an error when no failure_url is defined.
        """
        v = NoUrlView()
        self.assertRaises(NotImplementedError, v.get_failure_url)


class FormLabelSuffixTestCase(UnitTestCase):
    """Tests for the FormLabelSuffixMixin
    """
    def setUp(self):
        """Prepare the forms
        """
        self.form1 = LabelSuffixTestForm()
        self.form2 = LabelSuffixInClassTestForm()

    def test_suffix_override(self):
        """Label suffix should be overridden correctly
        """
        # Default is now empty string (not ':')
        self.assertEqual(self.form1.label_suffix, '')
        self.assertEqual(self.form2.label_suffix, '>')

    def test_suffix_preserved(self):
        """Label suffix is preserved if specified in custom label_tag call
        """
        # label_tag is only exposed on a BoundField, which a template obtains
        # by iterating the form's generator.
        for field in self.form1:
            self.assertTrue('::' in field.label_tag(label_suffix='::'))
