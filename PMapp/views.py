from django.shortcuts import render, redirect, get_object_or_404
from .forms import BS5RaceInfoForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Race
from django.urls import reverse_lazy

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
        return redirect('PMapp:Race_list')
    return render(request, 'PMapp/RaceInfo.html', {'form': form})

class Race_list(ListView):
    template_name = 'PMapp/Race_list.html'
    model = Race
     

class RaceDetail(DetailView):
    template_name = 'PMapp/Race_detail.html'
    model = Race

class RaceDelete(DeleteView):
    template_name = 'PMapp/Race_delete.html'
    model = Race
    success_url = reverse_lazy('PMapp:Race_list')

class RaceUpdate(UpdateView):
    template_name = 'PMapp/Race_update.html'
    model = Race
    fields = (
        'RaceName',
        'Category',
        'RaceDate',
        'Distance',
        'TimeLimit',
        'TargetTime',
        'Remarks',
        )
    success_url = reverse_lazy('PMapp:Race_list')

