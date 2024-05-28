from django.urls import path
from .views import home_page, battle_detail, battle_news, battles_page, gamer_register, gamer_login, blog_single, blog

urlpatterns = [
    path("", home_page, name='home-page'),
    path("battle_news/", battle_news, name='battle_news_page'),
    path("battles/", battles_page, name='battles_page'),
    path("battles/<int:battle_id>/", battle_detail, name='battle_detail'),

    path('register/', gamer_register, name='register'),
    path('login/', gamer_login, name='login'),
    path("blogs/<int:id>/", blog_single, name='blog-single'),
    path("blog/", blog, name='blog'),
]
