# Generated by Django 5.0.6 on 2024-05-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image_logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/assets/images/'),
        ),
    ]
