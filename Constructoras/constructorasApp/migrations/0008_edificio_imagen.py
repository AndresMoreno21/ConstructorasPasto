# Generated by Django 2.0.7 on 2018-07-24 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructorasApp', '0007_auto_20180723_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificio',
            name='imagen',
            field=models.ImageField(default=1, upload_to='fotosEdificios/'),
            preserve_default=False,
        ),
    ]
