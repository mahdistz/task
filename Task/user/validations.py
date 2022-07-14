import re
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


def is_valid_iran_national_code(national_code: str):
    if not re.search(r'^\d{10}$', national_code):
        return False

    check = int(national_code[9])
    s = sum(map(lambda x: int(national_code[x]) * (10 - x), range(0, 9))) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)


@deconstructible
class MobileNumberValidator(RegexValidator):
    # A rejection to check user input information
    regex = r"^[0][9]\d{9}$"

    message = (
        'Enter a valid mobile number. This value may contain only numbers.'
    )
    flags = 0


# create an instance from the class
mobile_number_validation = MobileNumberValidator()


@deconstructible
class TenDigitNumberValidator(RegexValidator):
    # A rejection to check user input information
    regex = r"^\d{10}$"

    message = (
        'Enter a valid number. This value may contain only numbers.'
    )
    flags = 0


# create an instance from the class
ten_digit_number_validation = TenDigitNumberValidator()
