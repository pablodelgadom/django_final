# Generated by Django 3.1.4 on 2021-04-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default=1, upload_to='photos/', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]