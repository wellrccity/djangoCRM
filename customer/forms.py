from django import forms
from .models import Customer

# Define o input para o tipo date
class DateInput(forms.DateInput):
    input_type = "date"

# Cria um formulário para cadastro de novos clientes
class CustomerForm(forms.ModelForm):

    # Campos de nome e sobrenome
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_lenght": "O nome não pode conter mais de 30 caracteres"}
        )

    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_lenght": "O sobrenome não pode conter mais de 50 caracteres"}
        )

    # Email
    email = forms.EmailField(label="Email")

    # Data de nascimento
    birth_date = forms.DateField(label="Nascimento", widget=DateInput())

    # DDD e telefone com regex para validar
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}",
        error_messages={"invalid": "Número de DDD inválido"}
        )

    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\+?1?[0-9]{8,9}",
        error_messages={"invalid": "Número de telefone inválido"}
        )

    # País, estado e cidade
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")

    # Define o model da classe e os campos do formulário
    class Meta:
        model = Customer
        fields = (
                "first_name", 
                "last_name", 
                "email", 
                "birth_date", 
                "area_code", 
                "phone_number", 
                "country", 
                "state", 
                "city"
        )