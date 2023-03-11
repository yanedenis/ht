from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie
from django.db.models import Q
from .forms import AddMovieForm, AddGenreForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def homePage(request):
    return render(request, "user/banner.html")

def topMovies(request):
    movie = Movie.objects.all()[:1]
    movies = Movie.objects.all()[:10]
    return render(request, "user/top-movies.html", {
        'movie': movie,
        'movies': movies,
    })

def allMovies(request, slug=None):
    genre = None
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        movies = Movie.objects.filter(Q(movieName__icontains=searchData) | Q(description__icontains=searchData))
    else:
        movies = Movie.objects.all()
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        movies = movies.filter(genre=genre)
    return render(request, 'user/all-movies.html', {
        'movies': movies,
        'genres': genres,
        'genre': genre,
    })

def movieDetail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'user/movie-detail.html', {
        'movie': movie
    })

def addMovie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allMovies')
    else:
        form = AddMovieForm()

    return render(request, 'admin/add-movie.html', {
        'form': form,
    })

def addGenre(request):
    if request.method == 'POST':
        form = AddGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allMovies')
    else:
        form = AddGenreForm()

    return render(request, 'admin/add-genre.html', {
        'form': form,
    })

def signUpPage(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    else:
        form = NewUserForm()
    return render(request, 'auth/sign-up.html', {
        'form': form,
    })

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('topMovies')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect('homePage')