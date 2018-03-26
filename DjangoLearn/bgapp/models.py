from django.db import models

"""
class UserTheme(models.Model):
    theme = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    rectime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_user_theme'
"""


class faith(models.Model):
    system_logo = models.CharField(max_length=100)
    beacon = models.CharField(max_length=100)
    banners = models.TextField()
    info = models.TextField()
    faith_logo = models.CharField(max_length=100)
    myinfo = models.TextField()
    ma_logo = models.CharField(max_length=100)

    class Meta:
        db_table = 'faith'

class hellomy(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'hello'