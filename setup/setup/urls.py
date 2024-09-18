from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from autenticacao import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', auth_views.registro, name='registro'),
    path('login/', auth_views.logar, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', auth_views.index, name='index'),
]

admin.site.site_header = "Conexão Solidária Admin"
admin.site.site_title = "Painel Administrativo"
admin.site.index_title = "Bem vindo ao painel do administrador!"