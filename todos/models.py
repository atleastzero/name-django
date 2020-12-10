from django.contrib.postgres.fields import ArrayField
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    reminder = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    repeat = models.DurationField(null=True, blank=True)
    def __str__(self):
        return self.title

class Routine(models.Model):
    title = models.CharField(max_length=200)
    order = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    todos = models.ManyToManyField(Todo)
    reminder = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    repeat = models.DurationField(null=True, blank=True)
    def __str__(self):
        return self.title

    def add_todo(self, todo):
        self.todos.add(todo)