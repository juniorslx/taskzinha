from django.db import models
from django.utils import timezone

class Mensagens(models.Model):
    nome = models.CharField(max_length=100)
    texto = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome}: {self.texto[:20]}"
