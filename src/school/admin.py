from django.contrib import admin

import school
from school.models import Group, Student

# Register your models here.
admin.site.register(Group)
admin.site.register(Student)