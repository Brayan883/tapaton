from django.urls import path
from django.contrib.auth import views as auth_views
from personal.views import aprendiz, equipo

urlpatterns = [
    path('aprendiz/', aprendiz, name='personal-aprendiz'),
    path('equipo/', equipo, name='personal-equipo'),
    
    # Logueo
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
    
]
