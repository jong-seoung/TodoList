from django.db import models
from accounts.models import User
from core.models import TimeStampedModel


class Todo(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_author')
    content = models.TextField()
    deadline_data = models.DateTimeField()
    is_finished = models.BooleanField()


class SupportTodo(models.Model):
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_user')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='support_todo')
    is_support = models.BooleanField(default=True)