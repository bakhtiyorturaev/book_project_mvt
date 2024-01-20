from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.


class CustomerUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+998\d{9}$', message="Telefon raqami quyidagi formatda kiritilishi kerak: '+998XXXXXXXXX'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=False)
    image_user = models.ImageField(default='users_images/user_default_image.jpg', upload_to='media')

    def __str__(self):
        return self.username
