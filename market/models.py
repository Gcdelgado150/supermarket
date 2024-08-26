import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    """
        - ID
        - CPF
        - Name
        - Gender
        - Subscription_type
    """
    GENDER_CHOICES = {
        'M': 'Male',
        'F': 'Female',
    }
    SUBS_CHOICES = {
        "D": "Dummy",
        "R": "Registered", 
        "P": "Pay", 
        "S": "Special",
    }
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    subscription_type = models.CharField(max_length=1, null=True, blank=True, choices=SUBS_CHOICES)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.name

class Supermarket(models.Model):
    """
        - ID
        - Name
        - City
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Supermercado"
        verbose_name_plural = "Supermercados"

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    """
    - ID
    - Name
    - Description
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    """
    - ID
    - Name
    - Value
    - Category
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self) -> str:
        return self.name

class Stocking(models.Model):
    """
    - Supermarket
    - Product
    - amount
    """
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"

    def __str__(self) -> str:
        return f"{self.supermarket} {self.product} - {self.amount}"

class Purchase(models.Model):
    """
    - Customer
    - Supermarket
    - Product
    - amount
    - date
    - payment_method
    """
    PAYMENT_CHOICES = {
        'C': 'Credit',
        'D': 'Debit',
        'P': 'Pix'
    }

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=1, null=True, blank=True, choices=PAYMENT_CHOICES)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self) -> str:
        return f"{self.supermarket} - {self.product}"