from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("app_pagina.urls", "app_pagina"))),
    path("cliente", include(("cliente.urls", "cliente"))),
]
