# Generated by Django 2.2.5 on 2019-10-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0008_auto_20191002_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='ciudad',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dirección',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='provincia',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono_movil',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono_particular',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
