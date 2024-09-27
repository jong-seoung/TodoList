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


class Alarm(models.Model):
    NOTIFICATION_TYPES = (
        ('follow', 'Follow'),
        ('support', 'Support'),
    )

    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarm_receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarm_sender')
    type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.type}"