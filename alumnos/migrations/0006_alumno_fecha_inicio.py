# Generated by Django 2.2.5 on 2019-10-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_auto_20191002_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
