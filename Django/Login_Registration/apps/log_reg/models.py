from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        for key in postData:
            if postData[key] == '':
                errors['empty_fields'] = 'All input fields must be filled'
        #querry a user object with the post email to see if it already exists in th edb
        try: 
            if User.objects.get(email=postData['email']):
                errors['not_unique'] = 'There is already a user with this email, please login.'
        except:
            pass
        if not postData['first_name'].isalpha() or len(postData['first_name']) < 2:
            errors['first_name'] = "First name must longer than 2 characters and contain no numbers"   
        if not postData['last_name'].isalpha() or len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must longer than 2 characters and contain no numbers"
        if not EMAIL_REGEX.match(postData['email']):
           errors['email'] = "you have entered an invalid email format"
        if len(postData['password']) < 8 or len(postData['confirm_password']) < 8:
            errors['password_length'] = 'password must be at least 8 characters'
        if postData['password'] != postData['confirm_password']:
            errors['password_match'] = "password and confirm do not match"
        return errors
    
    def password_hasher(self, pwd):
        password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        return password

    def login_validator(self, postData):
        errors = {}
        for key in postData:
            if postData[key] == '':
                errors['empty_fields'] = 'All input fields must be filled'
                return errors
        
        # find user in db
        this_user = User.objects.filter(email=postData['email']) #returns a queryset

        #this try and except is covers the case that the user info is not in the db since the filter query about could return an empty set...
        try:
            if not bcrypt.checkpw(postData['password'].encode(), this_user[0].password.encode()):
                errors['login_fail'] = 'user info does not match data base - please try again or register'
        except:
            errors['login_fail'] = 'user info does not match data base - please try again or register'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #sets up manager class for validations
    objects = UserManager()

    def __str__(self):
        return self.first_name
