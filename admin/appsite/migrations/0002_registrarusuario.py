# Generated by Django 4.2.3 on 2023-08-22 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=200)),
                ('Senha', models.CharField(max_length=200)),
                ('date_create', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
