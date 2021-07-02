from core import models


def listar_alunos():
    return models.Aluno.objects.all()
