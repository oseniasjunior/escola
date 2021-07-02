from django.db import models


class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descricao = models.CharField(db_column='tx_descricao', max_length=40, null=False, blank=False, unique=True)

    class Meta:
        db_table = 'estado_civil'
        managed = True

    def __str__(self):
        return self.descricao


# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', max_length=100, null=False, blank=False)
    estado_civil = models.ForeignKey(
        to='EstadoCivil',
        on_delete=models.DO_NOTHING,
        db_column='id_estado_civil',
        null=True,
        blank=True,
        related_name='alunos'
    )
    cursos = models.ManyToManyField(to='Curso', through='CursoAluno')

    class Meta:
        db_table = 'aluno'
        managed = True


class Curso(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', max_length=40, null=False, blank=False, unique=True)
    alunos = models.ManyToManyField(to='Aluno', through='CursoAluno')

    class Meta:
        db_table = 'curso'
        managed = True


class CursoAluno(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    aluno = models.ForeignKey(
        to='Aluno',
        on_delete=models.DO_NOTHING,
        db_column='id_aluno',
        null=False,
        blank=False
    )
    curso = models.ForeignKey(
        to='Curso',
        on_delete=models.DO_NOTHING,
        db_column='id_curso',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'curso_aluno'
        managed = True
        index_together = [
            ('aluno', 'curso',)
        ]
