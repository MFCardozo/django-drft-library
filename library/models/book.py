from django.db import models
from .author import Author


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    publication_date = models.DateField(verbose_name="Fecha de publicacion")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    pages = models.PositiveIntegerField(default=0, verbose_name="Paginas")
    authors = models.ManyToManyField(Author, related_name="books", verbose_name="Autores")

    class Meta:
        db_table = "books"
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def author_names(self) -> str:
        """get author's names from book."""
        return ", ".join(author.full_name for author in self.authors.all())
    
    author_names.short_description = "Autor/es"