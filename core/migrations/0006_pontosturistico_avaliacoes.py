# Generated by Django 3.2.16 on 2022-11-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_alter_avaliacao_nota'),
        ('core', '0005_pontosturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
