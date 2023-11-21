

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Prestamo',
            field=models.TextField(null=True, verbose_name='Prestamo'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Genero',
            field=models.CharField(max_length=60, verbose_name='Genero'),
        ),
    ]
