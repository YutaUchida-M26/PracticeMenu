# Generated by Django 3.2.5 on 2022-05-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMapp', '0005_auto_20220527_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='LapTime',
            field=models.IntegerField(blank=True, null=True, verbose_name='目標タイム(min)'),
        ),
    ]
