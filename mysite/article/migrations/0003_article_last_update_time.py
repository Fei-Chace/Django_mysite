# Generated by Django 2.0.4 on 2018-04-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
