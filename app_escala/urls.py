from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('', home, name='home' ),
    path('empresa/<str:pk_empresa>/', empresa_prestador, name='empresa'),
    path('empresa/', EmpresaView.as_view(), name='empresa_view'),
    path('empresa_update/<str:pk>/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresa_list', EmpresaListView.as_view(), name='empresa_list'),

    path('prestador/', PrestadorView.as_view(), name='prestador_view'),
    path('prestador_list/', PrestadorListView.as_view(), name='prestador_list'),
    path('prestador_update/<int:pk>', PrestadorUpdateView.as_view(), name='prestador_update'),

    path('especialidade/', EspecialidadeView.as_view(), name='especialidade_view'),
    path('especialidade_list/', EspecialidadeList.as_view(), name='especialidade_list'),
    path('especialidade_update/<str:pk>', EspecialidadeUpdate.as_view(), name='especialidade_update'),

    path('escala/', EscalaView.as_view(), name= 'escala_view'),
    path('escala_import/', import_csv, name= 'escala_import'),
    path('escala_copy/', EscalaViewCopy.as_view(), name= 'escala_copy'),
    path('escala_list/', EscalaListView.as_view(), name= 'escala_list'),
    path('escala/<int:pk>/', EscalaUpdateView.as_view(), name= 'escala_update'),
    path('escala_delete/<int:pk>/', EscalaDeleteView.as_view(), name= 'escala_delete'),
    path('escala_modelo', download_modelo, name= 'escala_modelo'),
    
    
    
]