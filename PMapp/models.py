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
    TimeLimit = models.IntegerField('時間制限(min)', blank=True)
    TargetTime = models.IntegerField('目標タイム(min)', blank=True)

    def __str__(self):
        return self.RaceName