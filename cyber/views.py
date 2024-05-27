from django.shortcuts import render
from django.views import View

from cyber.models import Battle, Battle_Group, Battle_News, Game_Club, Gamer


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


def gamer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        rating = request.POST['rating']
        game = request.POST['game']
        avatar = request.POST['avatar']

        Gamer.objects.create(username=username,
                             first_name=first_name,
                             last_name=last_name,
                             email=email,
                             password=password,
                             rating=rating,
                             game=game,
                             avatar=avatar)

    return render(request, 'register.html')