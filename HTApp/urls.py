from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('movies/top/', views.topMovies, name='topMovies'),
    path('movies/all/', views.allMovies, name='allMovies'),
    path('movies/all/filter/<slug:slug>/', views.allMovies, name='filterMovies'),
    path('movie/detail/<int:pk>/', views.movieDetail, name='movieDetail'),
    path('user/sign-up/', views.signUpPage, name='signUpPage'),
    path('user/login/', views.loginPage, name='loginPage'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
    path('admin/add-genre/', views.addGenre, name='addGenre'),
    path('admin/add-movie/', views.addMovie, name='addMovie'),
]
