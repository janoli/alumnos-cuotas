# Generated by Django 2.2.5 on 2019-10-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_auto_20191002_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cuota',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='curso',
            name='derexam',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
