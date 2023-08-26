from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set_permissions'
    )

    def __str__(self):
        return self.username


class Empleado(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)
