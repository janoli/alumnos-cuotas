# Generated by Django 2.2.5 on 2019-10-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0014_auto_20191004_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
    ]
