from django.db import models
from django.urls import reverse

"""
Controle das Escalas 

"""
class Base(models.Model):
    criacao = models.DateField('Data de Criacão', auto_now_add=True)
    modificacao = models.DateTimeField('Data de Modificação', auto_now=True)
    situacao = models.BooleanField('Situação', default=True)

    class Meta:
        abstract = True

class Empresa(Base):
    codigo = models.CharField('Codigo', max_length=60, null=False, blank=False, unique=True)
    nome = models.CharField('Nome', max_length=80, null=False, blank=False)
    #prestador = models.ManyToManyField(Prestador)


    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'
        ordering = ['nome']


class Prestador(Base):
    codigo = models.CharField('Codigo Prestador', max_length=15, blank=False, null=False, unique=True)
    nome = models.CharField('Nome Prestador', max_length=60, blank=False, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'


class Especialidade(Base):
    codigo = models.CharField('Codigo', max_length=3, null=True, blank=True, default='')
    nome = models.CharField('Codigo', max_length=35, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

class ProcedimentoSUS(Base):
    codigo = models.CharField('Codigo Procedimento', max_length=10)
    nome = models.CharField('Codigo Procedimento', max_length=260)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'



class Escala(Base):
    TIPO = [
        ('PRONTO SOCORRO', 'PRONTO SOCORRO'),
        ('AMBULATORIO', 'AMBULATORIO'),
        ('INTERNACAO', 'INTERNACAO'),
        ('EXAMES', 'EXAMES'),
    ]

    CONVENIO = [
        ('SUS', 'SUS'),
        ('CONVENIO', 'CONVENIO'),
        
    ]

    ESC = [
        ('PERIODO' , 'PERIODO'),
        ('PLANTAO' , 'PLANTAO'),
        ('PERIODO-RES', 'PERIODO-RES'),
        ('HORAS', 'HORAS'),
        ('QUANTIDADE', 'QUANTIDADE'),
    ]

    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    data_producao = models.DateField('Data Produção')
    data_pagamento = models.DateField()
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    porta = models.CharField(max_length=20, choices=TIPO)
    convenio = models.CharField(max_length=10, choices=CONVENIO)
    #servico = models.CharField(max_length=80)
    procedimento_sus = models.ForeignKey(ProcedimentoSUS, on_delete=models.CASCADE, null=True, blank=True, default='')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, null=True, blank=True)
    escala = models.CharField('escala', choices=ESC, max_length=20, default='', null=True, blank=True)
    

    class Meta:
        ordering = ['-modificacao']

