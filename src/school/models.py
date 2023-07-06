from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, related_name='Students')

    def __str__(self):
        return self.name + " " + self.lastname
