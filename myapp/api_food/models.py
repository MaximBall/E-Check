from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

class Customer(models.Model):

    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=20, verbose_name="Номер телефона", null=False, blank=False
    )

    def __str__(self):
        return "{}".format(self.user)

class Shop(models.Model):

    name_shop = models.CharField(
        max_length=40, verbose_name="Название", null=False, blank=False
    )

    adress = models.CharField(
        max_length=40, verbose_name="Адресс", null=False, blank=False
    )

    def __str__(self):
        return "{}".format(self.name_shop)
        
class Administrator(models.Model):

    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=20, verbose_name="Номер телефона", null=False, blank=False
    )
    shop_id = models.ForeignKey(
        Shop, verbose_name="Магазин", on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return "{}".format(self.user)

class Check(models.Model):

    user_id = models.ForeignKey(
        Customer, verbose_name="Покупатель", on_delete=models.CASCADE
    )
    shop_id = models.ForeignKey(
        Shop, verbose_name="Магазин", on_delete=models.CASCADE, default=1
    )
    products = models.JSONField()

    def __str__(self):
        return "{}".format(self.user_id)

class VerifyUser(models.Model):

    user_id = models.ForeignKey(
        Customer, verbose_name="Покупатель", on_delete=models.CASCADE
    )

    email_code = models.IntegerField()

    phone_code = models.IntegerField()

    def __str__(self):
        return "{}".format(self.user_id, self.email_code)


class Barcode(models.Model):

    user_id = models.ForeignKey(
        Customer, verbose_name="Покупатель", on_delete=models.CASCADE
    )

    verify_id = models.ForeignKey(
        VerifyUser, verbose_name="Проверка", on_delete=models.CASCADE
    )

    barcode = models.CharField(
        max_length=20, verbose_name="Штрих-код", null=False, blank=False
    )

    def __str__(self):
        return "{}".format(self.barcode)
