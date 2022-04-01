"""
models.py
"""
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """
    test that our todo items will be created
    by default with the done status of false
    """

    def test_done_defaults_to_false(self):
        """
        test for done default to false
        """
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """
        test string method
        """
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
