from django.contrib import admin
from .models import Empregado,Telefone,CPF,Departamento
# Register your models here.

class EmpregadoAdmin(admin.ModelAdmin):
    fields = ('nome','email')
    list_display = ('id','nome','email','endereco')
    list_filter = ('departamentos',)
    search_fields = ('id','nome','email')


admin.site.register(Empregado,EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)