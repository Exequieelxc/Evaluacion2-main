
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('Genero', models.CharField(max_length=20, verbose_name='Genero')),
                ('Autor', models.CharField(max_length=60, verbose_name='Autor')),
                ('Anio', models.IntegerField(max_length=20, verbose_name='Año')),
                ('Tamanio', models.CharField(max_length=60, verbose_name='Tamaño')),
            ],
        ),
    ]
