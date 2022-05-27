# Generated by Django 2.2.5 on 2022-05-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMapp', '0002_race_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MenuName', models.CharField(max_length=50, verbose_name='練習メニュー名')),
                ('Category', models.CharField(choices=[('bike_sun', 'バイク_晴'), ('bike_rai', 'バイク_雨'), ('run_sun', 'ラン_晴'), ('run_rai', 'ラン_雨'), ('swim_kick', 'スイム_キック'), ('swim_pull', 'スイム_プル'), ('swim_main', 'スイム_プル')], max_length=30, verbose_name='練習カテゴリ')),
                ('MenuLv', models.CharField(choices=[('Hard', '強め'), ('Midium', '普通'), ('Easy', '弱め')], max_length=30, verbose_name='練習強度')),
                ('Distance', models.IntegerField(verbose_name='1本あたりの距離(m)')),
                ('NumLap', models.IntegerField(blank=True, verbose_name='周回数')),
                ('LapTime', models.IntegerField(blank=True, verbose_name='目標タイム(sec)')),
                ('Remarks', models.TextField(blank=True, max_length=1000, verbose_name='備考')),
            ],
        ),
    ]
