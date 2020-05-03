from django import forms
from django_select2 import forms as s2form
from. models import Empresa, Prestador, Escala, Especialidade


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['codigo', 'nome', 'situacao']
        widgets = {
            'codigo'  : forms.TextInput(attrs={'class':'form-control'}),
            'nome'    : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador
        fields = ['codigo', 'nome', 'empresa', 'situacao']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class':'form-control'})
        }

class EspecialidadeForm(forms.ModelForm)       :
    class Meta:
        model = Especialidade
        fields = ['nome', 'situacao']
        widgets = {
            'nome'    : forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class DateInput(forms.DateInput):
    input_type = 'date'

class EscalaForm(forms.ModelForm):
    data_producao = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    data_pagamento = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    class Meta:
        model = Escala
        fields = ['prestador', 'data_producao', 'data_pagamento', 'quantidade', 'valor', 'porta', 'convenio', 'especialidade', 'escala', 'procedimento_sus']
        widgets = {
            'quantidade': forms.TextInput(attrs={'class':'form-control'}),
            'prestador' : forms.Select(attrs={'class':'form-control'}),
            #'prestador' : s2form.Select2Widget,
            'valor' : forms.NumberInput(attrs={'class':'form-control'}),
            'escala' : forms.Select(attrs={'class':'form-control'}),
            'porta' : forms.Select(attrs={'class':'form-control'}),
            'convenio' : forms.Select(attrs={'class':'form-control'}),
            'especialidade' : forms.Select(attrs={'class':'form-control'}),
            'procedimento_sus' : forms.Select(attrs={'class':'form-control'})
        }
