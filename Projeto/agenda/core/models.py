from django.db import models

class Agenda(models.Model):
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
