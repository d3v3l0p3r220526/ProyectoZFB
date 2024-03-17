from django.db import models
from django.contrib.auth.models import User

# Creando la tabla Task para insercion de clientes.
class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    documentId = models.IntegerField()
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    eps = models.CharField(max_length=50)
    arl = models.CharField(max_length=50)
    date_ini = models.DateField(null=True)
    date_end = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.empresa + '-by' + self.user.username

