from django.db import models

# Create your models here.
# Create a representaion of the database tables
class TodoList(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
