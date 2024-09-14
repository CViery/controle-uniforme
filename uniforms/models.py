from django.db import models

# Create your models here.
class Tamanhos(models.Model):
    tamanho = models.CharField(max_length=4)

    def __str__(self):
        return self.tamanho
    

class Categorias(models.Model):
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.categoria
    

class Uniforms(models.Model):
    codigo = models.CharField(max_length=10, null=True, unique=True)
    item = models.CharField(max_length=70)
    tamanho = models.ForeignKey(Tamanhos, on_delete=models.SET_NULL, null=True)  # Adiciona null=True já que SET_NULL exige isso
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.item
    

class Funcionario(models.Model):
    nome = models.CharField(max_length=70, null=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.nome
    

class Saida(models.Model):
    numero_de_saida = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    id_uniforme = models.ForeignKey(Uniforms, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()
    data_saida = models.DateTimeField()
    
    def __str__(self):
        return str(self.numero_de_saida)
    
class Entrada(models.Model):
    num_nota = models.CharField(max_length=10)
    data_emissao = models.DateField()  # Corrige o nome do campo para 'data_emissao' (sem acento)
    data_entrada = models.DateTimeField()
    uniforme = models.ForeignKey(Uniforms, on_delete=models.CASCADE)  # Adiciona on_delete
    quantidade = models.IntegerField()
    valor_uni = models.FloatField()
    valor_total = models.FloatField()

    def __str__(self):
        return self.num_nota
    
class CartTemp(models.Model):
    id_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Uniforms, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    
    