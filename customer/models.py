from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    # Cria tabela de clientes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Retorna nome e sobrenome quando a classe é chamada
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # Retorna o número de telefone completo quando a função é chamado
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"
    
    # Retorna nome e sobrenome quando a função é chamada
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Retorna cidade - estado quando a função é chamada
    def get_full_city(self):
        return f"{self.city} - {self.state}"
    
    # Retorna os dados do cliente
    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})
    
    # Deleta um cliente do banco
    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})
    
    # Define o nome da tabela
    class Meta:
        db_table = "costumer"