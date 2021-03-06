# Generated by Django 2.0.7 on 2018-07-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructorasApp', '0009_edificio_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificio',
            name='numero_de_apartamentos',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartamento',
            name='numero',
            field=models.CharField(help_text='Numero en el edificio', max_length=500),
        ),
    ]
