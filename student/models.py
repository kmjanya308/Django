from django.db import models


class Student_name(models.Model):
    nos = models.CharField(max_length=200)

    def __str__(self):
        return self.nos 
