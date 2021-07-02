from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']


@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
