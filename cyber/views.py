from django.shortcuts import render
from django.views import View

from cyber.models import Battle, Battle_Group, Battle_News, Game_Club


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
    return render(request, 'battle_detail.html', context)


def battle_news(request):
    battle_news = Battle_News.objects.all()
    context = {'battle_news': battle_news}
    return render(request, 'battles_news.html', context)