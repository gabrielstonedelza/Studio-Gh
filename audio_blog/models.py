from django.db import models

from django.utils.text import slugify
MOVIE_GENRE = (
    ("Free Style", "Free Style"),
    ("Dance Hall", "Dance Hall"),
    ("Gospel", "Gospel"),
    ("Jama", "Jama"),
    ("Hip Life", "Hip Life"),
    ("Adadam", "Adadam"),
)

AVAILABILITY = (
    ("On Air", "On Air"),
    ("Coming Soon", "Coming Soon"),
    ("Now Available", "Now Available"),
)


class StudioAudio(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=100, choices=MOVIE_GENRE)
    poster = models.ImageField(upload_to="audio_posters")
    availability = models.CharField(max_length=100, choices=AVAILABILITY)
    views = models.IntegerField(default=0)
    audio_link = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
