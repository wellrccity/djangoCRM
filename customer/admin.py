from django.contrib import admin
from .models import Customer

# Register your models here.

# Registra o model
@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    # Define as colunas que aparecerão na lista
    list_display = ["id", "first_name", "last_name", "email"]
