from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("principal.urls", "principal"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
]
