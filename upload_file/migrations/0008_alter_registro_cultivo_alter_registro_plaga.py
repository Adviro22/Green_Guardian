# Generated by Django 4.2.6 on 2024-01-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0007_alter_registro_cultivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cultivo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registro',
            name='plaga',
            field=models.IntegerField(default=0),
        ),
    ]
