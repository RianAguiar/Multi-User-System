from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentoForm
from .models import Documento

@login_required
def EnviarDocumento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.aluno = request.user
            doc.save()
            return redirect('enviar_documento')
    else:
        form = DocumentoForm()
    return render(request,'aluno/enviar.html', { 'form':form })

@login_required
def ListaDocumentos(request):
    docs = Documento.objects.select_related('aluno').all()
    return render(request, 'professor/lista.html', { 'docs': docs })
