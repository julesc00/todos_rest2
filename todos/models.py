from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
