from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):

    # Use email as the unique identifier
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'  # Use email as the default login field
    REQUIRED_FIELDS = []  # Remove 'email' from REQUIRED_FIELDS since it's now the USERNAME_FIELD

    # custom fields
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.email

