from functools import cache
from django.contrib import admin
from .models import (
    Customer, Shop, Check,
    Administrator, VerifyUser, Barcode
    )

admin.site.register(Customer)
admin.site.register(Shop)
admin.site.register(Check)
admin.site.register(Administrator)
admin.site.register(VerifyUser)
admin.site.register(Barcode)

