from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from .models import Book, Genre, Author
from django import forms
from django.utils.safestring import mark_safe

# admin.site.register(Books)
# admin.site.register(Genres)
# admin.site.register(Author)

admin.site.site_header = 'Bookstore'
admin.site.index_title = 'Моя супер админка'

@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')



class bookAdminForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = Book
        fields = '__all__'


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'date', 'author', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'author')
    list_filter = ('date', 'genres',)
    readonly_fields = ('get_big_image',)
    form = bookAdminForm

    @admin.display(description='Обложка')
    def get_image(self, item):
        return mark_safe(f'<img src="{item.inner_image.url}" width="100px">')

    @admin.display(description='Обложка')
    def get_big_image(self, item):
        return mark_safe(f'<img src="{item.inner_image.url}" width="100%">')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'born_and_death')
    list_display_links = ('id', 'full_name', 'born_and_death')
    search_fields = ('id', 'full_name', 'born_and_death')