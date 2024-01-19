from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    image_user = models.ImageField(default='users_images/user_default_image.jpg', upload_to='media')

    def __str__(self):
        return self.username
