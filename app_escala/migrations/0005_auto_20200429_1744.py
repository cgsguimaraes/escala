# Generated by Django 3.0.5 on 2020-04-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_escala', '0004_auto_20200429_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
