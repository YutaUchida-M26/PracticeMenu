from django.shortcuts import render, redirect, get_object_or_404
from .forms import BS5RaceInfoForm
from .models import Race

def RaceInfo(request):
    form = BS5RaceInfoForm(request.POST or None)
    if form.is_valid():
        race = Race()
        race.RaceName = form.cleaned_data['RaceName']
        race.Category = form.cleaned_data['Category']
        race.RaceDate = form.cleaned_data['RaceDate']
        race.Distance = form.cleaned_data['Distance']
        race.TimeLimit = form.cleaned_data['TimeLimit']
        race.TargetTime = form.cleaned_data['TargetTime']

        Race.objects.create(
            RaceName=race.RaceName,
            Category=race.Category,
            RaceDate=race.RaceDate,
            Distance=race.Distance,
            TimeLimit=race.TimeLimit,
            TargetTime=race.TargetTime,
        )
        return redirect('PMapp:race_list')
    return render(request, 'PMapp/RaceInfo.html', {'form': form})