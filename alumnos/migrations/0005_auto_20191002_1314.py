# Generated by Django 2.2.5 on 2019-10-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_alumno_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]