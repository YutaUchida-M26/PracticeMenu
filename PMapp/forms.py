from django import forms
from .models import Race

Athletic_CHOICES = [
   ('swim', '水泳大会'),
   ('bike', 'ロードレース'),
   ('run', '陸上大会'),
]

class BS5RaceInfoForm(forms.Form):
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
