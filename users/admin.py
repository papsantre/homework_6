from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'is_active', 'is_staff', 'is_superuser']


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'payment_sum', 'payment_method']
