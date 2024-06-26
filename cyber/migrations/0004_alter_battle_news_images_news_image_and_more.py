# Generated by Django 5.0.6 on 2024-06-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0003_updates_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle_news_images',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='game_club',
            name='game_club_image',
            field=models.ImageField(upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='avatar',
            field=models.ImageField(upload_to='media/avatars/'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image_logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='updates_news',
            name='updates_news_image',
            field=models.ImageField(upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='updates_news',
            name='updates_news_video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]
