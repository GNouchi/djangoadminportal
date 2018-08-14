from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length =255) 
    last_name = models.CharField(max_length =255) 
    email = models.CharField(max_length =255) 
    created_d = models.DateTimeField(auto_now_add = True)
    updated_d = models.DateTimeField(auto_now = True)