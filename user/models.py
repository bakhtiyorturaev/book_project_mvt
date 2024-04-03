from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    PHONE_REGEX = RegexValidator(regex=r'^\+998\d{9}$',
                                 message="Telefon raqami quyidagi formatda kiritilishi kerak: '+998XXXXXXXXX'.")
    phone_number = models.CharField(validators=[PHONE_REGEX], max_length=13, blank=False)
    image_user = models.ImageField(default='users_images/user_default_image.jpg', upload_to='media')
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

