from __future__ import unicode_literals
from django.db import models
from ..log_reg.models import User



# one author can have many books 
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

#one book can have many reviews and one user can write many reviews
class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews")
    stars = models.SmallIntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.content

    
