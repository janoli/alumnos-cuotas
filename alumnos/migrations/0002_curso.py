# Generated by Django 2.2.5 on 2019-09-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_text', models.CharField(max_length=40)),
                ('año_text', models.CharField(max_length=4)),
                ('cuota_text', models.IntegerField(null=True)),
                ('derexam_text', models.IntegerField(null=True)),
            ],
        ),
    ]
