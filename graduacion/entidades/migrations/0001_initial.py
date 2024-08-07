# Generated by Django 5.0.6 on 2024-07-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
                ('maestria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maestrías',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('modalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TrabajoDeGrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=30)),
                ('aprobado', models.BooleanField()),
            ],
        ),
    ]
