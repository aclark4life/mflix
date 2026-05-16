from django.views.generic import DetailView, ListView

from .models import Comment, MflixUser, Movie, Theater


class MovieListView(ListView):
    model = Movie
    template_name = "mflix/movie_list.html"
    context_object_name = "movies"
    paginate_by = 25


class MovieDetailView(DetailView):
    model = Movie
    template_name = "mflix/movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(movie_id=self.object.pk)[:10]
        return context


class CommentListView(ListView):
    model = Comment
    template_name = "mflix/comment_list.html"
    context_object_name = "comments"
    paginate_by = 25


class TheaterListView(ListView):
    model = Theater
    template_name = "mflix/theater_list.html"
    context_object_name = "theaters"
    paginate_by = 25


class UserListView(ListView):
    model = MflixUser
    template_name = "mflix/user_list.html"
    context_object_name = "users"
    paginate_by = 25
