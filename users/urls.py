from django.urls import path
from users import views
from movie.views import MovieList

app_name = 'users'

urlpatterns = [
    path("", MovieList.as_view(), name="movie_list"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),
]