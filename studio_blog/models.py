from django.db import models
from django.utils.text import slugify

MOVIE_GENRE = (
    ("Action", "Action"),
    ("Comedy", "Comedy"),
    ("Documentary", "Documentary"),
    ("Drama", "Drama"),
    ("Family", "Family"),
    ("Tv Shows", "Tv Shows"),
)

AVAILABILITY = (
    ("In Theaters", "In Theaters"),
    ("Coming Soon", "Coming Soon"),
    ("Now Available", "Now Available"),
)


class StudioMovies(models.Model):
    movie_title = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=100, choices=MOVIE_GENRE)
    poster = models.ImageField(upload_to="movie_posters")
    availability = models.CharField(max_length=100, choices=AVAILABILITY)
    views = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    movie_link = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_title

    def save(self, *args, **kwargs):
        value = self.movie_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_movie_poster(self):
        if self.poster:
            return 'http://127.0.0.1:8000' + self.poster.url
        return ""


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    caption = models.CharField(max_length=255, default="")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def get_image(self):
        if self.image:
            return "https://aglistudiosgh.xyz/" + self.image.url
        ""


class DuringProduction(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="Production Videos")
    poster = models.ImageField(upload_to="Poster",default="")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_video(self):
        if self.video:
            return "https://aglistudiosgh.xyz/" + self.video.url
        ""

    def get_poster(self):
        if self.poster:
            return "https://aglistudiosgh.xyz/" + self.poster.url
        ""

