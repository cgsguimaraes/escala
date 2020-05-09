import io
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django import forms
from django.forms.widgets import TextInput
from django.views.generic import FormView, UpdateView, CreateView, ListView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required

from .models import Empresa, Prestador, Escala, ProcedimentoSUS, Especialidade, Servico
from .forms import EmpresaForm, PrestadorForm, EscalaForm, EspecialidadeForm, ServicoForm
from .filters import EscalaFilter, PrestadorFilter, EmpresaFilter, EspecialidadeFilter, ServicoFilter

from app_escala.actions import export_xls

from excel_response import ExcelResponse
from openpyxl import Workbook



@login_required
def home(request):
    prestador = Prestador.objects.all()
    prestador_qt = prestador.count()

    empresa = Empresa.objects.all()
    empresa_qt = empresa.count()

    escala = Escala.objects.all()
    escala_qt = escala.count()

    context = {
        'prestador':prestador,
        'prestador_qt': prestador_qt,
        'empresa': empresa,
        'empresa_qt': empresa_qt,
        'escala' : escala,
        'escala_qt': escala_qt
    }
    return render(request, 'main.html', context)

def empresa_prestador(request, pk_empresa):
    empresa = Empresa.objects.get(pk=pk_empresa)
    prestadorFormSet = inlineformset_factory(Empresa, Prestador, 
                                                fields=('codigo', 'nome',) , 
                                                extra=1, 
                                                
                                                #widgets={
                                                 #      'codigo':TextInput(attrs={'class': 'form-control', 'placeholder':'Código'}),
                                                  #       'nome':TextInput(attrs={'class': 'form-control', 'placeholder':'Nome' })

                                                        #}
                                                        )
                                               
    if request.method == 'POST':
        formset = prestadorFormSet(request.POST, instance=empresa)
        if formset.is_valid():
            formset.save()
            redirect('home')
    
    formset = prestadorFormSet(instance=empresa)

    context = {
        'empresa': empresa,
        'formset': formset
    }


    return render(request, 'empresa/empresa_prestador.html' , context)


class EmpresaView(CreateView):
    template_name = 'empresa/empresa.html'
    form_class = EmpresaForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmpresaFilter(self.request.GET, queryset = self.get_queryset())
        return context



class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa.html'
    success_url = reverse_lazy('empresa_list')
    


class PrestadorView(CreateView):
    template_name = 'prestador/prestador.html'
    form_class = PrestadorForm
    success_url = reverse_lazy('prestador_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



class PrestadorListView(ListView):
    model = Prestador
    template_name = 'prestador/prestador_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PrestadorFilter(self.request.GET, queryset = self.get_queryset())
        return context


class PrestadorUpdateView(UpdateView):
    model = Prestador
    template_name = 'prestador/prestador.html'
    form_class = PrestadorForm
    success_url = reverse_lazy('prestador_list')


class EscalaView(CreateView):
    template_name = 'escala/escala.html'
    form_class = EscalaForm
    success_url = reverse_lazy('escala_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    


def save_data(data):
    aux = []
    for item in data:
        criacao = item.get('criacao')
        modificacao = item.get('modificacao')
        situacao = item.get('situacao')
        prestador_id = item.get('prestador_id')
        data_producao = item.get('data_producao')
        data_pagamento = item.get('data_pagamento')
        quantidade = item.get('quantidade')
        valor = item.get('valor')
        porta = item.get('porta')
        convenio = item.get('convenio')
        procedimento_sus_id = item.get('procedimento_sus_id')
        especialidade_id = item.get('especialidade_id')
        escala = item.get('escala')
        empresa_multi_id = item.get('empresa_multi_id')
        servico_escala_id = item.get('servico_escala_id')
        
        obj = Escala(
            criacao = criacao,
            modificacao = modificacao,
            situacao = situacao,
            prestador_id = prestador_id,
            data_producao = data_producao,
            data_pagamento = data_pagamento,
            quantidade = quantidade,
            valor = valor,
            porta = porta,
            convenio = convenio,
            procedimento_sus_id = procedimento_sus_id,
            especialidade_id = especialidade_id,
            escala = escala,
            empresa_multi_id = empresa_multi_id,
            servico_escala_id = servico_escala_id,
        )        
        aux.append(obj)
    Escala.objects.bulk_create(aux)
    

def import_csv(request):
    if request.method =='POST' and request.FILES['myfile']:
        myfyle = request.FILES['myfile']
        #lendo in memory
        file = myfyle.read().decode('ISO-8859-1')
        reader = csv.DictReader(io.StringIO(file), delimiter='|')
        #list comprehension
        data = [line for line in reader]
        save_data(data)
        return render(request, 'escala/success.html')
    template_name = 'escala/escala_import.html'
    return render(request, template_name)


def download_modelo(request):
    modelo = HttpResponse('escala-filter/media/teste.xlsx')
    return modelo


#classe teste para combobox
class EscalaViewCopy(CreateView):
    template_name = 'escala/escala_copy.html'
    form_class = EscalaForm
    success_url = reverse_lazy('escala_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)  


class PrestadorExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        return export_xls.plan_prestador()


   
    
class EscalaListView(ListView):
    model = Escala
    template_name = 'escala/escala_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EscalaFilter(self.request.GET, queryset= self.get_queryset())
        return context


class EscalaUpdateView(UpdateView):
    template_name = 'escala/escala.html'
    model = Escala
    form_class = EscalaForm
    success_url = reverse_lazy('escala_list')


class EscalaDeleteView(DeleteView):
    model = Escala
    template_name = 'escala/escala_delete.html'
    success_url = reverse_lazy('escala_list')


def exportar_modelo_excel(request):
    obj = Especialidade.objects.all()
    return ExcelResponse(obj)
    #filename = "modelo_importacao.xlsx"
    #wb = Workbook()
    #sheet = wb.active
    #sheet['A1'] = "Id"
    #sheet['B1'] = "Especialidade"
    #wb.save(filename=filename)


class EscalaExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        return export_xls.plan_escala()
    

@login_required
def escala_filter(request):
    #qs = ProcedimentoSUS.objects.all()
    qs_escala = Escala.objects.all()

    #buscar_texto = request.GET.get('buscar')

    #if buscar_texto != '' and buscar_texto is not None:
    #    qs = qs.filter(procedimento_sus__icontains=buscar_texto)

    
    form = EscalaForm()
    
    if request.method == 'POST':
        form = EscalaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {

        'qs' : qs_escala,
        'form' : form
    }
    return render(request, 'escala/escala.html', context)
    

class EspecialidadeView(CreateView):
    template_name = 'especialidade/especialidade.html'
    form_class = EspecialidadeForm
    success_url = reverse_lazy('especialidade_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



class EspecialidadeList(ListView):
    template_name = 'especialidade/especialidade_list.html'
    model = Especialidade

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EspecialidadeFilter(self.request.GET, queryset=self.get_queryset())
        return context



class EspecialidadeUpdate(UpdateView):
    template_name = 'especialidade/especialidade.html'
    model = Especialidade
    form_class = EspecialidadeForm
    success_url = reverse_lazy('especialidade_list')



class EspecialidadeExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        return  export_xls.plan_especialidade()
    


class ServicoView(CreateView):
    template_name = 'servico/servico.html'
    form_class = ServicoForm
    success_url = reverse_lazy('servico_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
     

class ServicoList(ListView):
    template_name = 'servico/servico_list.html'
    model = Servico
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServicoFilter(self.request.GET, queryset = self.get_queryset())
        return context


class ServicoUpdate(UpdateView):
    template_name = 'servico/servico.html'
    model = Servico
    form_class = ServicoForm
    success_url = reverse_lazy('servico_list')
