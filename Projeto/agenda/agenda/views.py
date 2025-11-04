from django.shortcuts import render, redirect
from .forms import ContatoForm
from .models import Contato

def novo_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')  # redireciona após salvar
    else:
        form = ContatoForm()
    return render(request, 'novo_contato.html', {'form': form})



def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'listar_contatos.html', {'contatos': contatos})
