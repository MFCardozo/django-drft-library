from django.contrib import admin
from .models.author import Author
from .models.book import Book



# Register author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "birth_date")
    search_fields = ("first_name", "last_name")


# Register book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date", "pages", "author_names")
    search_fields = ("title", "isbn")
    list_filter = ("publication_date",)
    filter_horizontal = ("authors",)