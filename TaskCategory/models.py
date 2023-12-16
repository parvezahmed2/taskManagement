from django.db import models
from TaskModel.models import Tasks
# Create your models here.


class TaskCategorys(models.Model):
    CategoryName = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Tasks)

    def __str__(self):
        return self.CategoryName
