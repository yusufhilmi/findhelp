# Generated by Django 3.0.7 on 2020-08-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200806_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name of User'),
        ),
    ]