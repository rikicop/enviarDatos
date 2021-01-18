from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.CharField(max_length=300, unique=False)

class Anpost(models.Model):
    titled= models.CharField(max_length=300, unique=True)
    contentd= models.CharField(max_length=300, unique=False)

class Comprar(models.Model):
    name = models.CharField(max_length=300, unique=True)
    department = models.CharField(max_length=300, unique=False)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=False)
    quantity = models.IntegerField(null=True, blank=False)
    

    def __str__(self):
        return str(self.name)
