# Generated by Django 2.2 on 2019-11-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0012_auto_20191121_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='titulo',
            field=models.CharField(default='', max_length=30, verbose_name='titulo'),
        ),
    ]
