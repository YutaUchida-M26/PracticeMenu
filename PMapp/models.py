from django.db import models

class Race(models.Model):
    """大会データベース"""
    Athletic_CHOICES = [
   ('swim', '水泳大会'),
   ('bike', 'ロードレース'),
   ('run', '陸上大会'),
]
    RaceName = models.CharField('大会名', max_length=50)
    Category = models.CharField('大会カテゴリ', max_length=30, choices=Athletic_CHOICES)
    RaceDate = models.DateTimeField('大会日')
    Distance = models.IntegerField('距離(m)')
    TimeLimit = models.IntegerField('時間制限(min)', blank=True, null=True)
    TargetTime = models.IntegerField('目標タイム(min)', blank=True, null=True)
    Remarks = models.TextField('備考', blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.RaceName
    
class Menu(models.Model):
    """メニューデータベース"""
    Athletic_CHOICES = [
   ('bike_sun', 'バイク_晴'),
   ('bike_rai', 'バイク_雨'),
   ('run_sun', 'ラン_晴'),
   ('run_rai', 'ラン_雨'),
   ('swim_kick', 'スイム_キック'),
   ('swim_pull', 'スイム_プル'),
   ('swim_main', 'スイム_メイン'),
    ]
    Lv = [
        ('Hard','強め'),
        ('Midium', '普通'),
        ('Easy', '弱め'),
        ]
    MenuName = models.CharField('練習メニュー名', max_length=50)
    Category = models.CharField('練習カテゴリ', max_length=30, choices=Athletic_CHOICES)
    MenuLv = models.CharField('練習強度', max_length=30, choices=Lv)
    Distance = models.IntegerField('1本あたりの距離(m)')
    NumLap = models.IntegerField('周回数', blank=True, null=True)
    LapTime = models.IntegerField('目標タイム(min)', blank=True, null=True)
    Remarks = models.TextField('備考', blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.MenuName