from uuid import uuid4


from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    job = models.CharField(max_length=225)
    address = models.JSONField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class userdetai(models.Model):
    name = models.CharField(max_length=255, )
    passwordc = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class trinerdetail(models.Model):
    Trainer_name = models.CharField(max_length=255)
    Course = models.CharField(max_length=255)
    Student_Name = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    Timeslate = models.CharField(max_length=255)

    def __str__(self):
        return self.Trainer_name
