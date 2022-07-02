# Generated by Django 4.0.4 on 2022-07-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudioMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Tv Shows', 'Tv Shows')], max_length=100)),
                ('poster', models.ImageField(upload_to='movie_posters')),
                ('availability', models.CharField(choices=[('In Theaters', 'In Theaters'), ('Coming Soon', 'Coming Soon'), ('Now Available', 'Now Available')], max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('movie_link', models.CharField(blank=True, max_length=300)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
