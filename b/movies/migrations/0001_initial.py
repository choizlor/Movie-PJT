# Generated by Django 3.2.13 on 2022-11-20 08:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('original_language', models.CharField(max_length=128)),
                ('adult', models.BooleanField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('release_date', models.DateField()),
                ('poster_path', models.CharField(max_length=128)),
                ('backdrop_path', models.CharField(max_length=128)),
                ('video', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=50)),
                ('first_actor', models.CharField(max_length=50)),
                ('second_actor', models.CharField(max_length=50)),
                ('third_actor', models.CharField(max_length=50)),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('rank', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
