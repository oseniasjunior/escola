# Generated by Django 3.2.5 on 2021-07-02 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210701_2102'),
    ]

    operations = [
        migrations.RunSQL(
            """
                INSERT INTO estado_civil (id, tx_descricao) VALUES (1, 'SOLTEIRO');
                INSERT INTO estado_civil (id, tx_descricao) VALUES (2, 'CASADO');
                INSERT INTO estado_civil (id, tx_descricao) VALUES (3, 'DIVORCIADO');
                INSERT INTO estado_civil (id, tx_descricao) VALUES (4, 'VIUVO');
            """
        )
    ]