from django.shortcuts import render
from django.views import View

from cyber.models import Battle


# Create your views here.

class BattleView(View):
    def get(self, request):
        battles = Battle.objects.all()
        context = {'battles': battles}
        return render(request, 'index.html', context)