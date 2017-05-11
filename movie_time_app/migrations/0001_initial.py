# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('year', models.IntegerField()),
                ('genres', models.CharField(max_length=200)),
                ('rating_median', models.FloatField()),
                ('rating_mean', models.FloatField()),
                ('relatable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity_score', models.FloatField()),
                ('first_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_movie', to='movie_time_app.Movie')),
                ('second_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_movie', to='movie_time_app.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('relevance', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_time_app.Movie')),
            ],
        ),
    ]
