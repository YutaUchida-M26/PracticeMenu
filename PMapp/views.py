from tempfile import tempdir
from django.shortcuts import render, redirect, resolve_url
from .forms import BS5RaceInfoForm, BS5MenuInfoForm, Calcurate_CalForm, LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .models import Race, Menu
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

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
        race.Remarks = form.cleaned_data['Remarks']

        Race.objects.create(
            RaceName=race.RaceName,
            Category=race.Category,
            RaceDate=race.RaceDate,
            Distance=race.Distance,
            TimeLimit=race.TimeLimit,
            TargetTime=race.TargetTime,
            Remarks = race.Remarks
        )
        return redirect('PMapp:Race_list')
    return render(request, 'PMapp/RaceInfo.html', {'form': form})

def MenuInfo(request):
    form = BS5MenuInfoForm(request.POST or None)
    if form.is_valid():
        menu = Menu()
        menu.MenuName = form.cleaned_data['MenuName']
        menu.Category = form.cleaned_data['Category']
        menu.MenuLv = form.cleaned_data['MenuLv']
        menu.Distance = form.cleaned_data['Distance']
        menu.NumLap = form.cleaned_data['NumLap']
        menu.LapTime = form.cleaned_data['LapTime']
        menu.Remarks = form.cleaned_data['Remarks']

        Menu.objects.create(
            MenuName=menu.MenuName,
            Category=menu.Category,
            MenuLv=menu.MenuLv,
            Distance=menu.Distance,
            NumLap=menu.NumLap,
            LapTime=menu.LapTime,
            Remarks=menu.Remarks,
        )
        return redirect('PMapp:Menu_list')
    return render(request, 'PMapp/MenuInfo.html', {'form': form})

def Calcurate_Cal(request):
    params = {
        'title':'Calcurate_Cal',
        'forms': Calcurate_CalForm(),
        'answer':'消費カロリーは、'
    }
    mets = [7, 9.8, 11.5, 14]
    if (request.method == 'POST'):
        if(request.POST['Category1'] == 'bike' and request.POST['Category2'] == 'Easy'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[1] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        elif(request.POST['Category1'] == 'bike' and request.POST['Category2'] == 'Midium'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[2] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        elif(request.POST['Category1'] == 'bike' and request.POST['Category2'] == 'Hard'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[3] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        elif(request.POST['Category2'] == 'Easy'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[0] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        elif(request.POST['Category2'] == 'Midium'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[1] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        elif(request.POST['Category2'] == 'Hard'):
            params['answer'] = '消費カロリーは、およそ' + str(mets[2] * int(request.POST['time']) * int(request.POST['weight']) * 1.05 / 60 ) + 'kcalです。'
        params['forms'] = Calcurate_CalForm(request.POST)
    return render(request, 'PMapp/Calcurate_Cal.html', params)

class Home(TemplateView):
    template_name = 'PMapp/Home.html'

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
    

class Menu_list(ListView):
    template_name = 'PMapp/Menu_list.html'
    model = Menu
     

class MenuDetail(DetailView):
    template_name = 'PMapp/Menu_detail.html'
    model = Menu

class MenuDelete(DeleteView):
    template_name = 'PMapp/Menu_delete.html'
    model = Menu
    success_url = reverse_lazy('PMapp:Menu_list')

class MenuUpdate(UpdateView):
    template_name = 'PMapp/Menu_update.html'
    model = Menu
    fields = (
        'MenuName',
        'Category',
        'MenuLv',
        'Distance',
        'NumLap',
        'LapTime',
        'Remarks',
        )
    success_url = reverse_lazy('PMapp:Menu_list')

class Login(LoginView):
    form_class = LoginForm
    template_name = 'PMapp/Login.html'

class Logout(LogoutView):
    template_name = 'PMapp/Logout.html'

'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

User = get_user_model()

class MyPage(OnlyYouMixin, DetailView):
    model = User
    template_name = 'PMapp/My_page.html'
    
class Signup(CreateView):
    template_name = 'PMapp/User_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('PMapp:Signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(TemplateView):
    template_name = 'PMapp/Signup_done.html'
    
'''ユーザー登録情報の更新'''
class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'PMapp/User_form.html'

    def get_success_url(self):
        return resolve_url('PMapp:My_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context
    
'''パスワード変更'''
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('PMapp:Password_change_done')
    template_name = 'PMapp/User_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


'''パスワード変更完了'''
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'PMapp/Password_change_done.html'