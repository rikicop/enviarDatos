# Generated by Django 2.2.11 on 2021-01-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviarApp', '0004_comprar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprar',
            name='department',
            field=models.CharField(max_length=300),
        ),
    ]
