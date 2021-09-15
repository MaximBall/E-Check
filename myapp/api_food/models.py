from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=20, verbose_name="Номер телефона", null=False, blank=False
    )

    def __str__(self):
        return "{}".format(self.user.username)