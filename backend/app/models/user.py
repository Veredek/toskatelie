from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    born_at = models.DateField(blank=True, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Artist(User):
    role = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"


class Customer(User):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"