from django.db import models

# Create your models here.


class myapp(models.Model):
    username = models.CharField(db_column='userName', max_length=32)  # Field name made lowercase.
    password = models.CharField(db_column='passWord', max_length=32)  # Field name made lowercase.
    url_login = models.CharField(db_column='url_login', max_length=200)