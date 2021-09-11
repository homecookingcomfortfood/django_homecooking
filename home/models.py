from django.db import models



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class smoothie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True,)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name


class receipe(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True,)
    ingre = models.TextField(null=True)
    desc1 = models.TextField(null=True)
    desc2 = models.TextField(null=True)
    desc3 = models.TextField(null=True)
    date = models.DateField()


    def __str__(self):
        return self.name

class frontimage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True,)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name