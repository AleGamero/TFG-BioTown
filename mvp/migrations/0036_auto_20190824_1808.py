# Generated by Django 2.2 on 2019-08-24 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0035_auto_20190824_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoaproductor',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='pedidoaproductor',
            name='consumidor',
        ),
    ]