# Generated by Django 2.2.4 on 2021-02-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
