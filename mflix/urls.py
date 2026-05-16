from django.urls import path

from . import views

app_name = "mflix"

urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
    path("movies/<pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("comments/", views.CommentListView.as_view(), name="comment-list"),
    path("theaters/", views.TheaterListView.as_view(), name="theater-list"),
    path("users/", views.UserListView.as_view(), name="user-list"),
]
