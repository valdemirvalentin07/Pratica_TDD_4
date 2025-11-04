from django.shortcuts import render, redirect
from core.forms import LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm
from django.http import Http404



def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})

        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context)


def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'listar_contatos.html', {'contatos': contatos})

def novo_contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_contatos')
    return render(request, 'novo_contato.html', {'form': form})

def editar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    form = ContatoForm(request.POST or None, instance=contato)
    if form.is_valid():
        form.save()
        return redirect('lista_edita')
    return render(request, 'editar_contato.html', {'form': form, 'contato': contato})

def excluir_contato(request, id):
    try:
        contato = Contato.objects.get(id=id)
    except Contato.DoesNotExist:
        # Aqui retornamos 404 explicitamente
        raise Http404("Contato não encontrado")

    if request.method == 'POST':
        contato.delete()
        return redirect('lista_exclui')

    return render(request, 'excluir_contato.html', {'contato': contato})

def lista_edita(request):
    contatos = Contato.objects.all()
    return render(request, 'lista_edita.html', {'contatos': contatos})

def lista_exclui(request):
    contatos = Contato.objects.all()
    return render(request, 'lista_exclui.html', {'contatos': contatos})
