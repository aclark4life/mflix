# mflix

A Django app demonstrating the [MongoDB Atlas `sample_mflix` dataset](https://www.mongodb.com/docs/atlas/sample-data/sample-mflix/).

Built with [`django-mongodb-backend`](https://pypi.org/project/django-mongodb-backend/) — a PyMongo-based Django database backend.

## Collections

| Collection | Model | Description |
|---|---|---|
| `movies` | `Movie` | Movie info: title, year, cast, ratings, awards |
| `comments` | `Comment` | User comments on movies |
| `theaters` | `Theater` | Theater locations with GeoJSON coordinates |
| `users` | `MflixUser` | Registered mflix users |

## Installation

Install the dependency (Django 6.0 required):

```bash
pip install django-mongodb-backend==6.0.*
```

Or install from the repo:

```bash
pip install -e .
```

## Integration

### 1. Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "mflix",
]
```

### 2. Configure the database

```python
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb_backend",
        "HOST": "mongodb://127.0.0.1:27017/",  # your MongoDB URI
        "NAME": "sample_mflix",
    }
}

DEFAULT_AUTO_FIELD = "django_mongodb_backend.fields.ObjectIdAutoField"
```

### 3. Wire up URLs

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("mflix/", include("mflix.urls")),
]
```

No migrations are needed — models use `managed = False` and map directly to the existing `sample_mflix` collections.

## Views

| URL | View | Description |
|---|---|---|
| `/mflix/movies/` | `MovieListView` | Paginated movie card grid (25/page) |
| `/mflix/movies/<id>/` | `MovieDetailView` | Movie detail with ratings, awards, and comments |
| `/mflix/comments/` | `CommentListView` | Paginated comment list |
| `/mflix/theaters/` | `TheaterListView` | Theater address cards with coordinates |
| `/mflix/users/` | `UserListView` | User table |

## Admin

All four models are registered in the Django admin with search, filtering, and appropriate `list_display` columns. Access at `/admin/` after creating a superuser.

## Templates

Templates live in `mflix/templates/mflix/` and use [Bootstrap 5](https://getbootstrap.com/) via CDN. Override any template in your project's template directory using the same path (e.g. `templates/mflix/base.html`).
