from email import charset
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    description = models.TextField(max_length=333)

    def __str__(self):
        return f"{self.title}"

