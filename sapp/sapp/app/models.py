from django.db import models

# Create your models here.
class Student(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    DoB = models.DateTimeField()
    Email = models.CharField(max_length=50)

    def __str__(self):
        return "ID: {}, Name: {}".format(self.ID, self.Name)