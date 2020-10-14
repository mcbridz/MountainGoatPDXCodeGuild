# Generated by Django 3.1.1 on 2020-10-08 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20201007_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='profile/images/200.jpg', null=True, upload_to='profile/images/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('deleted_comment', models.BooleanField(default=False)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post', to='blog_app.blogpost')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blog_app.comment')),
            ],
        ),
    ]