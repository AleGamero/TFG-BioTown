# Generated by Django 2.2 on 2019-08-27 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0039_auto_20190827_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('EnProceso', 'En proceso'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='EnProceso', max_length=20, verbose_name='Estado del pedido'),
        ),
    ]