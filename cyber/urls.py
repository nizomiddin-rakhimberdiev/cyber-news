from django.urls import path
from .views import BattleView
urlpatterns = [
    path("", BattleView.as_view(), name='battes-page')
]
