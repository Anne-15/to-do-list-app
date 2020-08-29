from django.db import models

# Create your models here.
# Create a representaion of the database tables
class Todo(models.Model):
    added_date = models.DateTimeField()
    todo_item = models.CharField(max_length=200)
