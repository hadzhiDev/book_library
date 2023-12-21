from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import main, full_book, about, books_by_genre
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', main, name='main'),
    path('books/<int:id>/', full_book, name='full_book'),
    path('about/', about, name='about'),
    path('books/', main, name='main2'),
    path('books/genre/<int:id>/', books_by_genre, name='books_by_genre'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
