# Generated by Django 3.0.5 on 2020-05-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_profiles_picture_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
