# Generated by Django 5.1 on 2024-12-03 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kriks_app', '0003_rename_cantidad_proveedores_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedores',
            old_name='horarios',
            new_name='horario',
        ),
    ]