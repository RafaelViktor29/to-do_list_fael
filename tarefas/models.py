from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    choices_stts = (('C', 'Concluída'), ('N', 'Não Concluída'))

    titulo = models.CharField(max_length=54)
    status = models.CharField(max_length=1, choices=choices_stts, default="N")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
