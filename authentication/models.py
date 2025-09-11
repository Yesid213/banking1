from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.TextField(max_length=5)
    id_country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Cities(models.Model):
    name = models.CharField(max_length=20)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name_cities = models.CharField(max_length=5)
    abrev = models.TextField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    id_city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
