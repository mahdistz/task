from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .validations import mobile_number_validation, is_valid_iran_national_code, ten_digit_number_validation
from .managers import UserManager


# Create your models here.
class Users(AbstractUser):
    """

    The first_name , last_name , username , email , password fields for the Users model
    are the same as the class AbstractUser fields .

    """
    national_code = models.CharField(max_length=10,
                                     validators=[is_valid_iran_national_code],
                                     )

    phone_number = models.CharField(max_length=11,
                                    validators=[mobile_number_validation],
                                    error_messages={
                                        'unique': "A user with that Phone number already exists.",
                                    },
                                    help_text='Example : 09125573688'
                                    )
    emergency_number = models.CharField(max_length=10, validators=[ten_digit_number_validation])  # شماره اضطراری
    birth_certificate_id = models.CharField(max_length=10, validators=[ten_digit_number_validation])  # شماره شناسنامه
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=25)
    address = models.TextField()
    home_number = models.CharField(max_length=3, validators=[RegexValidator(regex=r"[1-9]{1,3}")])  # پلاک
    postcode = models.CharField(max_length=10, validators=[ten_digit_number_validation])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    objects = UserManager()
