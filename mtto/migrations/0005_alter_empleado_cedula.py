# Generated by Django 4.0.3 on 2022-03-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0004_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
