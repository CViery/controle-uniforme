from django.contrib import admin
from uniforms.models import Tamanhos, Categorias, Uniforms, Funcionario, Saida, Entrada, CartTemp

# Register your models here.
class TamanhosAdmin(admin.ModelAdmin):
    ...

admin.site.register(Tamanhos, TamanhosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categorias, CategoriasAdmin)

class UniformesAdmin(admin.ModelAdmin):
    ...
admin.site.register(Uniforms, UniformesAdmin)

class FuncionariosAdmin(admin.ModelAdmin):
    ...
admin.site.register(Funcionario, FuncionariosAdmin)

class SaidasAdmin(admin.ModelAdmin):
    ...

admin.site.register(Saida, SaidasAdmin)

class EntradasAdmin(admin.ModelAdmin):
    ...
admin.site.register(Entrada, EntradasAdmin)

class CartTempAdmin(admin.ModelAdmin):
    ...
admin.site.register(CartTemp, CartTempAdmin)