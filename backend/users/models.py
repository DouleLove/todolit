import time

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models
from django.utils.translation import gettext_lazy as _


class User(django.contrib.auth.models.AbstractUser):

    def generate_avatar_path(self, filename: str) -> str:
        return f'uploads/{self.id}/{time.time()}_{filename}'

    def __str__(self) -> str:
        return self.username

    visible_username = django.db.models.CharField(
        _('visible username'),
        max_length=150,
        help_text=_('non-unique username which is preferably '
                    'visible for the other users'),
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator],
        null=True,
    )
    avatar = django.db.models.ImageField(
        _('avatar'),
        upload_to=generate_avatar_path,
    )

    # removing email, first_name, last_name fields from the model
    email = None
    first_name = None
    last_name = None

    # cleaning up AbstractUser's attributes which link to the email field
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
