from django.contrib import admin

from .models import Comment, MflixUser, Movie, Theater


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "rated", "runtime", "imdb_rating", "num_mflix_comments")
    list_filter = ("type", "rated")
    search_fields = ("title", "cast", "directors", "genres")
    readonly_fields = ("imdb", "tomatoes", "awards", "genres", "cast", "directors", "writers", "languages", "countries")

    def imdb_rating(self, obj):
        return obj.imdb_rating

    imdb_rating.short_description = "IMDb"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "movie_id", "date", "short_text")
    search_fields = ("name", "email", "text")
    readonly_fields = ("movie_id",)

    def short_text(self, obj):
        return obj.text[:80]

    short_text.short_description = "Comment"


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ("theaterId", "city", "state", "zipcode")
    search_fields = ("theaterId",)
    readonly_fields = ("location",)

    def city(self, obj):
        return obj.address.get("city", "")

    def state(self, obj):
        return obj.address.get("state", "")

    def zipcode(self, obj):
        return obj.address.get("zipcode", "")


@admin.register(MflixUser)
class MflixUserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    exclude = ("password",)
