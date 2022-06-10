from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title='Test todo',
            body='This is a test'
        )

    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        self.assertEqual(todo.title, 'Test todo')
        self.assertEqual(todo.body, 'This is a test')