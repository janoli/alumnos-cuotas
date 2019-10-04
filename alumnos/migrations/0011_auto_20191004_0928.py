# Generated by Django 2.2.5 on 2019-10-04 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0010_auto_20191002_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nivel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='fecha_baja',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='fecha_inscripcion',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(null=True)),
                ('concepto', models.CharField(max_length=3, null=True)),
                ('detalle', models.CharField(max_length=30, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('medio_de_pago', models.CharField(choices=[('EF', 'EFECTIVO'), ('DE', 'DEBITO'), ('CR', 'CREDITO')], default='EF', max_length=2)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
            ],
        ),
    ]
