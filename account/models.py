from django.db import models
from django.contrib.auth.models import User as user_admin

# Create your models here.
rols = (
    ("admin", "admin"),
    ("employer", "employer"),
    ("help desk", "help desk"),
    ("technicien", "technicien"),
)


class User(models.Model):
    user =models.ForeignKey(user_admin,related_name='user',on_delete=models.CASCADE)
    name = models.CharField( max_length = 20)
    last_name = models.CharField( max_length = 20)
    mail = models.EmailField( max_length = 20)
    role = models.CharField(
        max_length = 20,
        choices = rols,
        default = '1')
    password = models.CharField( max_length = 21)

    def __str__(self):
        return self.name


