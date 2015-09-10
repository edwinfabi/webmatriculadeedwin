from django.contrib import admin
from carga.models import Curso, Ciclo, NaturalPerson
# Register your models here.


class NaturalPersonAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("last_name", "first_name", "birth_date")
    search_fields = ("last_name", "first_name", "birth_date",)

admin.site.register(NaturalPerson, NaturalPersonAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("codigo", "nombre", "user")
    search_fields = ("nombre", "codigo",)

admin.site.register(Curso, CursoAdmin)


class CicloAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ("abrev", "desc")
    search_fields = ("abrev", "desc",)

admin.site.register(Ciclo, CicloAdmin)
