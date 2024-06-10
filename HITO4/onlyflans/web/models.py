import uuid
from django.db import models



class CategoriasProducto(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    
    class Meta:
            verbose_name_plural = "Categorias de productos"
            
    def __str__(self):
        return self.name
    
    
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoriasProducto)
    class Meta:
            verbose_name_plural = "Productos"
            
    def __str__(self):
        return self.name
    
class ContacForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    class Meta:
            verbose_name_plural = "Formulario de Contacto"
            
    def __str_(self):
        return self.customer_name