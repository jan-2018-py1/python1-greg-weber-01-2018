from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Course name must longer than 5 characters"
        if len(postData['description']) < 16:
            errors['description'] = "Course description must longer than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

    def __str__(self):
        return self.name


class Description(models.Model):
    summary = models.TextField()
    course = models.OneToOneField(Course)


