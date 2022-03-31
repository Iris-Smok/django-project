"""
tests for form
"""
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """
    tests for form fields
    """

    def test_item_name_is_required(self):
        """
        tesst for name required
        """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """
        test for done field not required
        """
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        test for fields in form
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
