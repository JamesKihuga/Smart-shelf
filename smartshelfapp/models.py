from django.db import models


# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    department = models.CharField(max_length=40)
    store = models.CharField(max_length=50)
    email =models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
     return self.username

class Shelf(models.Model):
    number = models.IntegerField()
    location = models.CharField(max_length=50)
    date = models.DateField()
    due_date = models.DateField()
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.number

class Client(models.Model):
     name = models.CharField(max_length=60)
     username = models.CharField(max_length=30)
     contact = models.CharField(max_length=20)
     address = models.CharField(max_length=10)
     email = models.EmailField()

     def __str__(self):
         return self.name

class  Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

