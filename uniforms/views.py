from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entrada, Uniforms, Funcionario, CartTemp, Saida
import random
from datetime import datetime

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'uniforms/pages/home.html')

@csrf_exempt
def cadastros(request):
    return render(request, 'uniforms/pages/cadastro.html')

@csrf_exempt
def saidas(request):
    uniformes = Uniforms.objects.all()
    funcionarios = Funcionario.objects.all()
    button_enviar = False
    return render(request, 'uniforms/pages/saida.html', context={
        'uniformes': uniformes,
        'funcionarios': funcionarios,
        'button_enviar': button_enviar
    })

@csrf_exempt
def entradas(request):
    uniformes = Uniforms.objects.all()
    return render(request, 'uniforms/pages/entrada.html', context={
        'uniformes': uniformes
    })

@csrf_exempt
def efetuar_entrada(request):
    if request.method == "POST":
        num_nota = request.POST.get('num_nota')
        data_emissao = request.POST.get('data_emissao')
        data_entrada = request.POST.get('data_entrada')
        uniforme_nome = request.POST.get('uniforme')  # Nome do uniforme
        quantidade = int(request.POST.get('quantidade'))
        valor_uni = float(request.POST.get('valor_uni'))
        valor_total = float(request.POST.get('valor_total'))

        # Busca o uniforme pelo nome
        try:
            uniforme = Uniforms.objects.get(codigo=uniforme_nome)
        except Uniforms.DoesNotExist:
            return HttpResponse("Uniforme não encontrado.", status=404)

        # Cria a entrada no banco de dados
        entrada = Entrada(
            num_nota=num_nota,
            data_emissao=data_emissao,
            data_entrada=data_entrada,
            uniforme=uniforme,  # Usa o objeto Uniforms
            quantidade=quantidade,
            valor_uni=valor_uni,
            valor_total=valor_total
        )
        entrada.save()

        # Atualiza a quantidade no modelo Uniforms
        uniforme.quantidade_estoque += quantidade
        uniforme.save()

        return HttpResponse('success_url', status=200)  # Redireciona para uma página de sucesso ou outra página desejada
    else:
        return HttpResponse("Método não permitido.", status=405)
    
@csrf_exempt
def carrinho_saida(request):
    if request.method == "POST":
        resposta = ''
        funcionario_id = request.POST.get('funcionario')
        uniforme_id = request.POST.get('uniforme')
        quantidade = request.POST.get('quantidade')

        # Armazenar o ID do funcionário na sessão
        request.session['funcionario_id'] = funcionario_id

        # Buscar a instância do Funcionario e do Uniform
        funcionario = Funcionario.objects.get(id=funcionario_id)
        uniforme = Uniforms.objects.get(codigo=uniforme_id)
        solicitado = int(quantidade)
        verificar_estoque = int(uniforme.quantidade_estoque)
        if verificar_estoque == 0:
            resposta = 'produto em falta'
        else:
            if solicitado > verificar_estoque:
               resposta = 'quantidade invalida'
            else:
                carrinho = CartTemp(
                    id_funcionario=funcionario,
                    id_produto=uniforme,
                    quantidade=quantidade
                )
                carrinho.save()
                resposta = 'Produto adicionado'
    # Buscar todos os dados necessários
    dados = CartTemp.objects.filter(id_funcionario=funcionario_id)
    uniformes = Uniforms.objects.all()
    funcionarios = Funcionario.objects.all()

    # Recuperar o ID do funcionário da sessão, se existir
    funcionario_id = request.session.get('funcionario_id', None)
    funcionario_selecionado = Funcionario.objects.filter(id=funcionario_id).first() if funcionario_id else None
    button_enviar = True
    # Renderizar o template com o contexto
    return render(request, 'uniforms/pages/saida.html', context={
        'carrinho': dados,
        'funcionarios': funcionarios,
        'uniformes': uniformes,
        'funcionario': funcionario_selecionado,
        'resposta': resposta,
        'button_enviar': button_enviar
    })

@csrf_exempt
def enviar(request):
    if request.method == 'POST':
        carrinho = CartTemp.objects.all()
        numero_saida = random.randint(1, 100)
        for item in carrinho:
            agora = datetime.now()
            

            saida = Saida(
                numero_de_saida = numero_saida,
                funcionario = item.id_funcionario,
                id_uniforme = item.id_produto,
                quantidade = item.quantidade,
                data_saida = agora
            )
            saida.save()
            CartTemp.objects.all().delete()

        return HttpResponse('saida_url')  # Redireciona para a página de saída ou onde desejar
    