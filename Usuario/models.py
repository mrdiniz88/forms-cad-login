from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):

    def __str__(self):
        return self.username

