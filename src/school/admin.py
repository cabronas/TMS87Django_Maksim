from django.contrib import admin

import school
from school.models import Group, Student, Diary, Book

# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Diary)
admin.site.register(Book)