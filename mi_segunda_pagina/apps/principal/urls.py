from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("principal/planes", views.planes, name="planes"),
    path("principal/sedes", views.sedes, name="sedes"),
    path("principal/filosofia", views.filosofia, name="filosofia"),
    path("principal/quienes_somos", views.quienes_somos, name="quienes_somos"),
    path("principal/maquinas", views.maquinas, name="maquinas"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="principal/logout.html"), name="logout"),
    path("principal/registrado", views.registrado, name="registrado"),
    path("principal/about", views.about, name="about"),
    
]
