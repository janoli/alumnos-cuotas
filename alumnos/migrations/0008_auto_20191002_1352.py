# Generated by Django 2.2.5 on 2019-10-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_auto_20191002_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='apellido_text',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='dni_text',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='nombre_text',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='año_text',
            new_name='año',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='cuota_text',
            new_name='cuota',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='curso_text',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='derexam_text',
            new_name='derexam',
        ),
    ]
