from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from cyber.models import Battle, Battle_Group, Battle_News, Game_Club, Gamer, Updates_news
from cyber.forms import GameCommentaryForm


# Create your views here.


def home_page(request):
    battles = Battle.objects.all()
    battle_groups = Battle_Group.objects.all()
    game_clubs = Game_Club.objects.all()
    context = {
        'battles': battles,
        'battle_groups': battle_groups,
        'game_clubs': game_clubs,
    }
    return render(request, 'index.html', context)


def battle_detail(request, battle_id):
    battle = Battle.objects.get(pk=battle_id)
    battle_groups = Battle_Group.objects.all().filter(battle_id__id=battle_id)
    context = {'battle': battle, 'battle_groups': battle_groups}
    return render(request, 'matches-single.html', context)


def battle_news(request):
    battle_news = Battle_News.objects.all()
    context = {'battle_news': battle_news}
    return render(request, 'battles_news.html', context)


def battles_page(request):
    battles = Battle.objects.all()
    battle_groups = Battle_Group.objects.all()
    context = {'battles': battles, "battle_groups": battle_groups}
    return render(request, 'matches.html', context)


def blog(request):
    updates = Updates_news.objects.all()
    context = {'updates': updates}
    return render(request, 'blog.html', context)


def blog_single(request, id):
    update = Updates_news.objects.get(id=id)
    context = {'update': update}
    return render(request, 'blog-single.html', context)


def gamer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home-page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def gamer_register(request):
    if request.method == 'POST':
        form = GameCommentaryForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(gamer_login)
    else:
        form = GameCommentaryForm()
        context = {'form': form}

    return render(request, 'register.html', context)
