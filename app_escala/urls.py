from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('', home, name='home' ),
    path('escala/empresa/<str:pk_empresa>/', empresa_prestador, name='empresa'),
    path('escala/empresa/', EmpresaView.as_view(), name='empresa_view'),
    path('escala/empresa_update/<str:pk>/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('escala/empresa_list', EmpresaListView.as_view(), name='empresa_list'),
    path('escala/empresa_excel', EmpresaExcel.as_view(), name='empresa_excel'),

    path('escala/prestador/', PrestadorView.as_view(), name='prestador_view'),
    path('escala/prestador_list/', PrestadorListView.as_view(), name='prestador_list'),
    path('escala/prestador_update/<int:pk>', PrestadorUpdateView.as_view(), name='prestador_update'),
    path('escala/prestador_excel', PrestadorExcel.as_view(), name='prestador_excel'),

    path('escala/especialidade/', EspecialidadeView.as_view(), name='especialidade_view'),
    path('escala/especialidade_list/', EspecialidadeList.as_view(), name='especialidade_list'),
    path('escala/especialidade_update/<str:pk>', EspecialidadeUpdate.as_view(), name='especialidade_update'),
    path('escala/especialidade_excel', EspecialidadeExcel.as_view(), name='especialidade_excel'),

    path('escala/servico/', ServicoView.as_view(), name='servico_view'),
    path('escala/servico_list/', ServicoList.as_view(), name='servico_list'),
    path('escala/servico_update/<str:pk>', ServicoUpdate.as_view(), name='servico_update'),
    path('escala/servico_excel', ServicoExcel.as_view(), name='servico_excel'),

    path('escala/escala/', EscalaView.as_view(), name= 'escala_view'),
    path('escala/escala_import/', import_csv, name= 'escala_import'),
    path('escala/escala_copy/', EscalaViewCopy.as_view(), name= 'escala_copy'),
    path('escala/escala_list/', EscalaListView.as_view(), name= 'escala_list'),
    path('escala/escala/<int:pk>/', EscalaUpdateView.as_view(), name= 'escala_update'),
    path('escala/escala_delete/<int:pk>/', EscalaDeleteView.as_view(), name= 'escala_delete'),
    path('escala/escala_modelo_excel', exportar_modelo_excel, name='escala_modelo_excel'),
    path('escala/escala_modelo', EscalaExcel.as_view(), name='escala_modelo'),
    
    
    
]