from django.db import models

# Create your models here.
class Course(models.Model):
    image = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=200)

    # __ string representation of an object
    # self first parameter of a class
    def __str__(self):
        return self.summary