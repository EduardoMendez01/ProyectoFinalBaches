from django.contrib import admin
from .models import Usuario, reportes, admintrar

# Register your models here.
admin.site.register(Usuario)
admin.site.register(reportes)
admin.site.register(admintrar)