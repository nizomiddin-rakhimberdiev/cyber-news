from django.urls import path
from .views import home_page, battle_detail, battle_news, battles_page
urlpatterns = [
    path("", home_page, name='home-page'),
    path("battle_news/", battle_news, name='battle_news_page'),
    path("battles/", battles_page, name='battles_page'),
    path("battles/<int:battle_id>/", battle_detail, name='battle_detail'),
]
