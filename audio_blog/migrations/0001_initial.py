# Generated by Django 4.0.4 on 2022-04-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudioAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('genre', models.CharField(choices=[('Free Style', 'Free Style'), ('Dance Hall', 'Dance Hall'), ('Gospel', 'Gospel'), ('Jama', 'Jama'), ('Hip Life', 'Hip Life'), ('Adadam', 'Adadam')], max_length=100)),
                ('poster', models.ImageField(upload_to='audio_posters')),
                ('availability', models.CharField(choices=[('On Air', 'On Air'), ('Coming Soon', 'Coming Soon'), ('Now Available', 'Now Available')], max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('audio_link', models.CharField(blank=True, max_length=300)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
