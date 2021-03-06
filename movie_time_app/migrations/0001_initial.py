# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 17:28
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
                ('year', models.IntegerField(null=True)),
                ('genres', models.CharField(max_length=200)),
                ('num_ratings', models.IntegerField(null=True)),
                ('rating_median', models.FloatField(null=True)),
                ('rating_mean', models.FloatField(null=True)),
                ('relatable', models.BooleanField(default=True)),
                ('liked_or_not', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OnlineLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_time_app.Movie')),
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
