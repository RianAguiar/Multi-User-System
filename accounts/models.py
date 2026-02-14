from django.db import models
from django.contrib.auth.models import User

# classe para criar usuario e atribui-lo à um perfil(aluno ou professor)
class Perfil (models.Model):
    tipo_usuario = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        )
    user = models.models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=tipo_usuario)
    def __str__(self):
        return f"{self.user.username} - {self.tipo}"