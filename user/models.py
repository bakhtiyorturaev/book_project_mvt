from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+998\d{9}$',
                                 message="Telefon raqami quyidagi formatda kiritilishi kerak: '+998XXXXXXXXX'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=False)
    image_user = models.ImageField(default='users_images/user_default_image.jpg', upload_to='media')

    def __str__(self):
        return self.username



#
# # Create your models here.
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(_('The Email field must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# def create_superuser(self, email, password=None, **extra_fields):
#     extra_fields.setdefault('is_staff', True)
#     extra_fields.setdefault('is_superuser', True)
#
#     return self.create_user(email, password, **extra_fields)
#
