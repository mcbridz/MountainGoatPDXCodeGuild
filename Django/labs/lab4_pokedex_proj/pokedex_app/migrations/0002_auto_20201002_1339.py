# Generated by Django 3.1.1 on 2020-10-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(),
        ),
    ]
