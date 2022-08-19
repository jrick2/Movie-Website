from django.urls import path
from movie.views import MovieList, MovieDetail
from users import views

urlpatterns = [
    path("", MovieList.as_view(), name="movie_list"),
    path('<int:pk>', MovieDetail.as_view(), name="movie_detail"),
    path("sign_up", views.sign_up, name="sign_up" ),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),

]