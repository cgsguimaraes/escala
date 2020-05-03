from django.contrib import admin
from .models import Empresa, Prestador, Escala, Especialidade, ProcedimentoSUS
# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'criacao', 'modificacao', 'situacao']


@admin.register(Prestador)
class PrestadorAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'criacao', 'modificacao', 'situacao']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['prestador', 'data_producao', 'data_pagamento', 'quantidade', 'valor', 'escala', 'porta', 'convenio', 'especialidade']


@admin.register(Especialidade)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome']

@admin.register(ProcedimentoSUS)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome']