from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("principal/planes", views.planes, name="planes"),
    path("principal/sedes", views.sedes, name="sedes"),
    path("principal/filosofia", views.filosofia, name="filosofia"),
    path("principal/quienes_somos", views.quienes_somos, name="quienes_somos"),
    path("principal/maquinas", views.maquinas, name="maquinas"),
    
    
]
