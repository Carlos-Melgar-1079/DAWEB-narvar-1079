# Generated by Django 5.1.3 on 2024-11-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='direccion',
            new_name='total',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(verbose_name='fecha de compra'),
        ),
    ]