# Generated by Django 3.0.6 on 2020-05-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articles_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
