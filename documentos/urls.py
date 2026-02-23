from django.urls import path
from . import views

app_name = 'documentos'

urlpatterns = [
    path('EnviarDocumento/', views.EnviarDocumento, name='enviar'),
    path('ListaDocumentos/', views.ListaDocumentos, name='lista'),
]