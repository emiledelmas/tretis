# Generated by Django 3.0.5 on 2020-05-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_historique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historique',
            name='username',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
