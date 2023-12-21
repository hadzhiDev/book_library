from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    full_name = models.CharField(verbose_name = 'имя автора', max_length=150, unique=True)
    born_and_death = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.full_name}'


class Genre(models.Model):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(verbose_name = 'название', max_length=150, unique=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='books_images/', verbose_name='обложка')
    inner_image = models.ImageField(upload_to='books_images/', verbose_name='внутренная обложка')
    description = models.CharField(max_length=1000, verbose_name='Краткое описание')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр', related_name='books')
    file = models.FileField(upload_to='books_pdf/', verbose_name='файл')
    date = models.DateField(auto_now_add=True, verbose_name='дата добавление')
    author = models.ForeignKey(Author, verbose_name = 'Автор', on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.name}'