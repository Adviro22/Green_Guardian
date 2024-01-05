# Generated by Django 4.2.6 on 2024-01-05 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_result', '0001_initial'),
        ('upload_file', '0004_registro_imagen_binaria_alter_registro_cultivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.planta', verbose_name='Tipo de Planta'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='plaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_result.plaga', verbose_name='Tipo de Planta'),
        ),
    ]
