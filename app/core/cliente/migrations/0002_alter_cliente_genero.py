# Generated by Django 3.2.9 on 2021-11-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(max_length=1, verbose_name='Género'),
        ),
    ]