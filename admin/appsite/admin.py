from django.contrib import admin
from .models import Site
from .models import RegistrarUsuario

# Register your models here.
admin.site.register(Site)
admin.site.register(RegistrarUsuario)
