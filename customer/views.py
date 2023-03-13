from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Cria uma listview dos clientes
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"    
    paginate_by = 5 # Paginação de 5 itens por página
    model = Customer # models.py
    
    # Função para busca
    def get_queryset(self):
        name = self.request.GET.get("name")
        # Verifica se o usuário está tentando fazer uma busca
        if name:
            # Busca os clientes por nome e/ou sobrenome
            object_list = self.model.objects.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
                )
        else:
            # Quando não há busca
            object_list = self.model.objects.all()
        return object_list


# Cria a view da lista de clientes
class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("customer:customer-list")
    
# Cria a view com os dados de um cliente
class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    # Se o cliente não existir retorna erro 404
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)
    

    def get_success_url(self):
        return reverse("customer:customer-list")

# Recarrega a lista após deletar um cliente  
class CustomerDeleteView(DeleteView):

    # Se o cliente a ser deletado não existir retorna 404
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id) 

    def get_success_url(self):
        return reverse("customer:customer-list")