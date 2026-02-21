from django.db import models
from django.contrib.auth.models import User

class Documento(models.Model):
    status = (
        ('enviado', 'Enviado'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
        )
    
    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documentos_enviados'
        )
    
    professor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='documentos_avaliados'
        )
    status = models.CharField(
        max_length=10,
        choices=status,
        default='enviado'
        )

    titulo = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='documentos/')
    feedback = models.TextField(blank=True,null=True)
    def __str__(self):
        return f"{self.titulo} - {self.aluno.username}"
