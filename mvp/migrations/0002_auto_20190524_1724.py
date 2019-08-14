# Generated by Django 2.2 on 2019-05-24 17:24

from django.db import migrations, models
import mvp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=mvp.models.fotoBlog_directory_path, verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=mvp.models.fotoProductos_directory_path, verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='fotoLogo',
            field=models.FileField(blank=True, null=True, upload_to=mvp.models.fotoLogo_directory_path, verbose_name='Logo'),
        ),
    ]