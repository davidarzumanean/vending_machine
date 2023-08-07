from django.contrib import admin
from apps.vending.models import Product
from apps.vending.models import User

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock"]

admin.site.register(Product, ProductAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "user_name", "balance"]

admin.site.register(User, UserAdmin)