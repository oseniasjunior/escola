# Generated by Django 3.2.5 on 2021-07-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='tx_nome', max_length=100)),
            ],
            options={
                'db_table': 'aluno',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='tx_nome', max_length=40, unique=True)),
            ],
            options={
                'db_table': 'curso',
                'managed': True,
            },
        ),
    ]
