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


class Diary(models.Model):
    avg_score = models.DecimalField(max_digits=4, decimal_places=2)
    student = models.OneToOneField(
        'Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name='Diary'
    )

    def __str__(self):
        return self.student.name + " " + self.student.lastname + " " + str(self.avg_score)


class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField(max_length=100)
    students = models.ManyToManyField(
        'Student',
        related_name='Books'
    )

    def __str__(self):
        return self.name