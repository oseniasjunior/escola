# Generated by Django 3.2.5 on 2021-07-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_aluno_estado_civil'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='cs_sexo', max_length=1, null=True),
        ),
    ]
