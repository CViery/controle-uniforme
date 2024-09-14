from django.urls import path
from uniforms.views import home, entradas, saidas, cadastros, efetuar_entrada, carrinho_saida, enviar

urlpatterns = [
    path('', home),
    path('cadastros/', cadastros),
    path('saida/', saidas, name='saida'),
    path('entrada/', entradas),
    path('processar_formulario/', efetuar_entrada, name='processar_formulario'),
    path('saida/carrinho/', carrinho_saida ),
    path('saida/enviar/', enviar )
]
