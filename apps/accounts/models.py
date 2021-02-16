from django.db import models
from django.contrib.auth.models import User, AbstractUser

import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=None, editable=False)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.pk = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return "@{}".format(self.username)
