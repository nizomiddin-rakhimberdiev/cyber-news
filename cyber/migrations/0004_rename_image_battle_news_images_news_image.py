# Generated by Django 5.0.6 on 2024-05-11 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0003_alter_battle_news_images_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battle_news_images',
            old_name='image',
            new_name='news_image',
        ),
    ]