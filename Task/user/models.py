from django.contrib.auth.models import AbstractUser
from django.db import models
from .validations import mobile_number_validation, is_valid_iran_national_code
from .managers import UserManager


# Create your models here.
class Address(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=25)
    address = models.TextField()
    home_number = models.IntegerField(max_length=5)  # پلاک
    postcode = models.IntegerField(max_length=10)


class Users(AbstractUser):
    national_code = models.CharField(max_length=10,
                                     validators=[is_valid_iran_national_code],
                                     )

    phone_number = models.CharField(max_length=11,
                                    unique=True,
                                    validators=[mobile_number_validation],
                                    error_messages={
                                        'unique': "A user with that Phone number already exists.",
                                    },
                                    help_text='Example : 09125573688'
                                    )
    emergency_number = models.CharField(max_length=11)  # شماره اضطراری
    birth_certificate_id = models.IntegerField(max_length=10)  # شماره شناسنامه
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    objects = UserManager()
