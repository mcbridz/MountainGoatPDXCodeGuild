# Generated by Django 3.1.1 on 2020-10-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20201006_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.CharField(max_length=10000),
        ),
    ]