# Generated by Django 3.2.16 on 2022-11-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
