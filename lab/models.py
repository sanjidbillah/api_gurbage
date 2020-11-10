from django.db import models


# Create your models here.

class MyModel(models.Model):
    username = models.CharField(max_length=200)
    city = models.TextField()


class ChildTable(models.Model):
    mobile = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    married = models.BooleanField()

