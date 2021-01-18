# Generated by Django 2.2.11 on 2021-01-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enviarApp', '0003_auto_20200713_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('department', models.CharField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
    ]
