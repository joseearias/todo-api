from django.contrib.auth import get_user_model
from django.db import models

class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
