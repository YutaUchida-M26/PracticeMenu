from django import forms
from .models import Race

class BS5RaceInfoForm(forms.Form):
    Athletic_CHOICES = [
   ('swim', '水泳大会'),
   ('bike', 'ロードレース'),
   ('run', '陸上大会'),
]
    RaceName = forms.CharField(
        #'大会名', 
        max_length=50,
        required=True,
        )
    Category = forms.ChoiceField(
        #'大会カテゴリ',
        widget=forms.Select, 
        choices=Athletic_CHOICES,
        required=True,
        )
    RaceDate = forms.DateTimeField(
        #'大会日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
        )
    Distance = forms.IntegerField(
        #'距離(m)',
        required=True,
        )
    TimeLimit = forms.IntegerField(
        #'時間制限(min)', 
        required=False,
        )
    TargetTime = forms.IntegerField(
        #'目標タイム(min)',
        required=False,
        )
    Remarks = forms.CharField(
        widget=forms.Textarea,
        required=False,
        )


class BS5MenuInfoForm(forms.Form):
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
    MenuName = forms.CharField(
        max_length=50,
        required=True,
        )
    Category = forms.ChoiceField( 
        choices=Athletic_CHOICES,
        required=True,
        )
    MenuLv = forms.ChoiceField(
        choices=Lv,
        required=True,
        )
    Distance = forms.IntegerField(
        required=True,
        )
    NumLap = forms.IntegerField(
        required=False,
        )
    LapTime = forms.IntegerField(
        required=False,
    )
    Remarks = forms.CharField(
        required=False, 
        widget=forms.Textarea,
        )
    
class Calcurate_CalForm(forms.Form):
    Athletic_CHOICES = [
   ('swim', '水泳'),
   ('bike', '自転車'),
   ('run', 'ランニング'),
    ]
    Lv = [
        ('Hard','強め'),
        ('Midium', '普通'),
        ('Easy', '弱め'),
        ]
    Category1 = forms.ChoiceField(
        label='種目',
        widget=forms.Select, 
        choices=Athletic_CHOICES,
        required=True,
        )
    Category2 = forms.ChoiceField(
        label='強度',
        widget=forms.Select, 
        choices=Lv,
        required=True,
        )
    time = forms.IntegerField(required=True,label='時間(min)')
    weight = forms.IntegerField(required=True,label='体重(kg)')