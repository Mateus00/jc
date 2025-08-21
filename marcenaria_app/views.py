from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Secao, Categoria, Galeria, Produto, Pagina
from django.utils.text import slugify

def home(request):
    secoes_all = Secao.objects.all()
    destaques = Produto.objects.filter(destaque=True).select_related('categoria')
    secoes = {slugify(secao.titulo): secao for secao in secoes_all}
    
    galeria = Galeria.objects.all()
    
    logo = Pagina.objects.first()

    categorias = Categoria.objects.prefetch_related('produtos')
    carrosses_dinamicos = []
    for categoria in categorias:
        produtos = categoria.produtos.all()
        if produtos:
            carrosses_dinamicos.append({'titulo': categoria.nome, 'produtos': produtos})

    return render(request, 'home.html', {
        **secoes,
        'galeria': galeria,
        'carrosseis': carrosses_dinamicos,
        'carrossel_destaques': destaques,
        'logo': logo
    })

def contato(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        whatsapp = request.POST.get('whatsapp')
        email = request.POST.get('email')
        messages.success(request, "Obrigado por entrar em contato! Retornaremos em breve.")
        return redirect('contato')
    return render(request, 'contato.html')
