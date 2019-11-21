# Generated by Django 2.2 on 2019-11-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0010_libro_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=255, verbose_name='Título')),
                ('fecha_de_compra', models.DateField(verbose_name='Fecha de publicación')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=220)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
        migrations.AddField(
            model_name='comentario',
            name='producto_id',
            field=models.ManyToManyField(to='libro.Producto'),
        ),
    ]
