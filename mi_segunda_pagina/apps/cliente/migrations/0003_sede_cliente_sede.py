# Generated by Django 5.0.1 on 2024-02-07 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_rename_pais_origen_id_cliente_pais_origen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.sede'),
        ),
    ]
