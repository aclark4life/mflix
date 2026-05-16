from django.db import models
from django_mongodb_backend.fields import ObjectIdField, ArrayField


class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.IntegerField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    released = models.DateTimeField(null=True, blank=True)
    plot = models.TextField(blank=True, default="")
    fullplot = models.TextField(blank=True, default="")
    poster = models.URLField(max_length=1000, blank=True, default="")
    type = models.CharField(max_length=50, blank=True, default="")
    rated = models.CharField(max_length=20, blank=True, default="")
    lastupdated = models.CharField(max_length=50, blank=True, default="")
    num_mflix_comments = models.IntegerField(default=0)

    # Array fields
    genres = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    cast = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    directors = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    writers = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    languages = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    countries = ArrayField(models.CharField(max_length=100), blank=True, default=list)

    # Nested document fields
    imdb = models.JSONField(null=True, blank=True)
    tomatoes = models.JSONField(null=True, blank=True)
    awards = models.JSONField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "movies"
        ordering = ["-year", "title"]

    def __str__(self):
        return f"{self.title} ({self.year})"

    @property
    def imdb_rating(self):
        if self.imdb and isinstance(self.imdb, dict):
            return self.imdb.get("rating")
        return None

    @property
    def tomatoes_viewer_rating(self):
        if self.tomatoes and isinstance(self.tomatoes, dict):
            viewer = self.tomatoes.get("viewer", {})
            return viewer.get("rating") if viewer else None
        return None


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    movie_id = ObjectIdField()
    text = models.TextField()
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "comments"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.name} — {self.text[:60]}"


class Theater(models.Model):
    theaterId = models.IntegerField()
    location = models.JSONField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "theaters"
        ordering = ["theaterId"]

    def __str__(self):
        loc = self.location or {}
        addr = loc.get("address", {})
        city = addr.get("city", "")
        state = addr.get("state", "")
        return f"Theater #{self.theaterId} — {city}, {state}"

    @property
    def address(self):
        if self.location and isinstance(self.location, dict):
            return self.location.get("address", {})
        return {}

    @property
    def geo(self):
        if self.location and isinstance(self.location, dict):
            return self.location.get("geo")
        return None


class MflixUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = "users"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
