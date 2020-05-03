import django_filters
from django import forms
from django.db import models
from .models import Escala, Prestador, Empresa, Especialidade

class EscalaFilter(django_filters.FilterSet):
    class Meta:
        model = Escala
        
        fields = {
            'porta': ['icontains'],
            'data_producao':['year'],
            'data_pagamento' : ['month','year'],
            'convenio' : ['icontains'],
            'prestador' : ['exact'],
            'escala': ['icontains'],
            'especialidade': ['exact']
            }

        
class PrestadorFilter(django_filters.FilterSet):
    class Meta:
        model = Prestador

        fields = {
            'codigo': ['icontains'],
            'nome': ['icontains'],
            'empresa': ['exact']
        }
    


class EmpresaFilter(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'codigo': ['icontains'],
            'nome': ['icontains'],
            'situacao': ['exact'] 
        }


class EspecialidadeFilter(django_filters.FilterSet):
    class Meta:
        model = Especialidade
        fields = {
            'codigo': ['icontains'],
            'nome': ['icontains']
        }