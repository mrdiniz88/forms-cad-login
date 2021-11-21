from django.urls import path
from . import views

app_name = 'Usuario'

urlpatterns = [
    path('cadastro/', views.usuario_cadastro, name='cadastro'),
    path('login/', views.usuario_login, name='login'),
    path('logout/', views.usuario_logout, name='logout'),
]