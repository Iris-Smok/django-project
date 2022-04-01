"""
test for views.py
"""
from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    """
    tests for views
    """
    def test_get_todo_list(self):
        """
        get the home page, todo_list
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """
        get add_item page
        """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """
        get edit_item_page
        """
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """
        add item
        """
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """
        delete item
        """
        # first we will creata an item
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        # make sure view redirect us
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """
        toggle item
        """
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        # make sure view redirect us
        self.assertRedirects(response, '/')
        update_item = Item.objects.get(id=item.id)
        self.assertFalse(update_item.done)

    def test_can_edit_item(self):
        """
        test for post method for edit view
        """
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        update_item = Item.objects.get(id=item.id)
        self.assertEqual(update_item.name, 'Updated Name')
