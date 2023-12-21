from django.shortcuts import render, get_object_or_404
from core.models import Book, Genre


def main(request):
    search = request.GET.get('search', None)
    if search:
        books = Book.objects.filter(name__icontains=search)
    else:
        books = Book.objects.all()
    genre_id = request.GET.get('genre', None)
    if genre_id:
        genre = get_object_or_404(Genre, id=int(genre_id))
        books = books.filter(genres=genre)
    genres = Genre.objects.all()
    return render(request, 'index.html', { 'books_list': books, 'genres': genres,})


def full_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'full_book.html', { 'book': book,})


def about(request):
    genres = Genre.objects.all()
    return render(request, 'about.html', {'genres': genres} )


def books_by_genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    books = Book.objects.filter(genres=genre)
    genres = Genre.objects.all()
    return render(request, 'index.html', { 'books_list': books, 'genres': genres, })